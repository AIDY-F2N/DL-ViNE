# ONLY THE FIRST TIME 
#import Pkg
#Pkg.add(["JSON", "Graphs", "MetaGraphs", "DataStructures", "StatsBase", "Random", "Statistics", "JLD2"])


import JSON
using Graphs, MetaGraphs, DataStructures, StatsBase, Random, Statistics, JLD2

include("utils.jl")
include("direct-link_mapping.jl")
include("checks.jl")
include("node_mapping.jl")

function NRPA(sn::MetaGraph{Int64, Float64},
    vnr::MetaGraph{Int64, Float64}, 
    level::Int64, N::Int64, 
    policy::Union{DefaultDict{String, Float64, Float64}, Dict{String, Float64}}, 
    solver::Function,
    max_bw_sn,
    max_bw_vnr,
    sum_bw_sn,
    sum_bw_vnr) 

    if level == 0
        # copying is slow
        # we don't use modifications to vnr for reward calculations
        # hence do not copy it as it consumes lots of time
        # as a result, after NRPA, vnr contains the last calculated embedding, which is not the best one

        score, sequence = playout(copy_graph(sn), vnr, policy, solver, max_bw_sn, max_bw_vnr, sum_bw_sn, sum_bw_vnr)

        return score, sequence
    else
        best_score::Float64 = -9999
        best_seq = Int64[]
        for i = 1:N
            reward, sequence = NRPA(sn, vnr, level - 1, N, policy, solver, max_bw_sn, max_bw_vnr, sum_bw_sn, sum_bw_vnr)
                                    
            if reward > best_score
                best_score = reward
                best_seq = sequence
            end
            if reward > 0
                policy = adapt(policy, best_seq, copy_graph(sn), vnr, solver, max_bw_sn, max_bw_vnr, sum_bw_sn, sum_bw_vnr)
            end
        
        end

        return best_score, best_seq
    end
end

function run_nepa(instance_path,
             linkPlacement, 
             level,
             N,
             log_file)


    # do not use DefaultDict as it will initialize all lists with different references to the same list
    scores = Dict{Int64, Vector{Any}}()
    
    events, instance = load_instance(instance_path)
    # sn loaded once
    sn = instance[-1]
    future_leaves = Int64[]
    arv = 0
    accepted::Int64 = 0
    refused::Int64 = 0

    while !isempty(events)
        check_bounds_are_respected(sn)
        q::Float64, type::String, slice::Int64 = popfirst!(events)
        if type == "arrival"
            arv += 1
            vnr = instance[slice]
            policy = Dict{String, Float64}()
            sn_prec = copy_graph(sn)
            #reorder vnr so the first node treated is the one with the least legal moves
            vnr = reorder_vnr(vnr, sn, max_bw_sn(sn), max_bw_vnr(vnr), sum_bw_sn(sn), sum_bw_vnr(vnr))
            instance[slice] = vnr
         

            score,seq =  @time NRPA(sn, vnr, level, N, policy, linkPlacement,max_bw_sn(sn), 
                            max_bw_vnr(vnr), sum_bw_sn(sn), sum_bw_vnr(vnr))

            #println("Peut on utiliser futureSeq ? : $use_futureSeq")
            if score > 0
                curr_node = 1
                sn_2 = copy_graph(sn)
                vnr_2 = instance[slice]
                for action in seq
                    sn_2, vnr_2, curr_node, rw, done = play(sn_2, vnr_2, curr_node, action, linkPlacement)
                    if done
                        sn = sn_2
                        vnr = vnr_2
                    end
                end

                if !haskey(scores, nv(vnr))
                    scores[nv(vnr)] = []
                end
                
                #Que pour l'affichage du vrai reward 
                success=true
                r::Float64=calculateReward(sn,vnr,success)
                push!(scores[nv(vnr)], r)
                #=
                println("VNR numéro : $slice")
                for e in edges(vnr)
                    p = props(vnr, e)
                    chemin=p[:vlink]
                    len=length(chemin)
                    println("Le chemin est : $chemin, lenght $len")
                end=#

                #=
                println("SN AFTER VNE")
                for v in 1:nv(sn)
                    cpu_u=get_prop(sn,v,:cpu_used)
                    cpu_m=get_prop(sn,v,:cpu_max)
                    println("Noeud $v cpu used = $cpu_u, cpu max = $cpu_m")
                end
                =#
                #println("Seq is : $seq ,Reward : $score, realREward : $r")

                
                instance[slice] = vnr
                push!(future_leaves, slice)
                accepted += 1
                check_each_vn_uses_resource_amount(sn, sn_prec, vnr)  
                check_each_vl_uses_resource_amount(sn, sn_prec, vnr)  
            else
                refused += 1
            end

        else
            if issubset([slice], future_leaves)
                vnr = instance[slice]
                remove!(future_leaves, slice)
                free_cpu_bw(sn, vnr)
            end
        end
        
        
    
    end

    stats, glob_r_c = get_stats(scores, accepted)
 
    print("********* Number of accepted slices using NRPA-DL = $accepted\n")
    open(log_file,"a") do io
        print(io,accepted, ",", glob_r_c)
    end
end


function main(instance_path, log_file, level, N, seed)
    Random.seed!(seed)
    linkPlacement = place_links_dl
    t = @elapsed run_nepa(instance_path, linkPlacement, level, N, log_file) 
    open(log_file,"a") do io
        println(io, ",", t)
    end
end



main(ARGS[1], ARGS[2], parse(Int64,ARGS[3]), parse(Int64, ARGS[4]), parse(Int64,ARGS[5]))