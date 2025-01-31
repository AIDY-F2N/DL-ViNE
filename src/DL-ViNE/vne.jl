include("bestFitNode.jl")
include("dlink.jl")

function VNE(sn, vnr, policy, solver::Function, max_bw_sn, max_bw_vnr, sum_bw_sn, sum_bw_vnr)
    sequence = []
    done::Bool = false
    curr_node = 1
    # each key identifies a state uniquely in our dictionnary
    key = ""
    reward::Float64 = 0
    while true
        if done
            return reward, sequence
        end
        if !haskey(policy, key)
            default_weight!(policy, key)
        end
        z::Float64 = 0.0
        weights_vect = Float64[]
        actions_vect = Int64[]
        legalMoves= get_legal_moves(sn, vnr, curr_node, max_bw_sn, max_bw_vnr, sum_bw_sn, sum_bw_vnr)
        normalWay = true
        for m in legalMoves
            if bestFitNode(m,curr_node, vnr, sn)==true 
                normalWay = false
                key_child = key * "," * string(m)
                if !haskey(policy, key_child)
                    default_weight!(policy, key_child)
                end
                if !isempty(sequence)
                    if m in sequence
                        policy[key_child] += 2
                    end
                end

                ex = exp(policy[key_child])
                z += ex
                push!(actions_vect, m)
                push!(weights_vect, ex)
            end 
        end
        if normalWay == true
            for m in legalMoves
                key_child = key * "," * string(m)
                if !haskey(policy, key_child)
                    default_weight!(policy, key_child)
                end
                if !isempty(sequence)
                    if m in sequence
                        policy[key_child] += 2
                    end
                end
                ex = exp(policy[key_child])
                z += ex
                push!(actions_vect, m)
                push!(weights_vect, ex)
            end 
        end
        # if there is no more move here, it means the placement is failed since it is unfinishable
        if  length(actions_vect) == 0
            return 0, []
        end
        # sample actions according to Gibbs sampling
        action = sample(actions_vect, Weights(weights_vect ./ z), 1)[1]
        sn, vnr, curr_node, reward, done = play(sn, vnr, curr_node, action, solver)   
        push!(sequence, action)
        key *= ","
        key *= string(action)
    end
end


function play(sn::MetaGraph{Int64, Float64},
    vnr::MetaGraph{Int64, Float64},
    curr_node::Int64,
    action::Int64,
    solver::Function)

    cpu_used::Int64 = get_prop(sn, action, :cpu_used)
    cpu::Int64 = get_prop(vnr, curr_node, :cpu)

    # if the chosen node (action) has not enough cpu, failure
    if get_prop(sn, action, :cpu_max) - cpu_used < cpu 
        return sn, vnr, curr_node, 0, true
    else
        # else update sn & vnr
        set_prop!(sn, action, :cpu_used, cpu_used + cpu)
        set_prop!(vnr, curr_node, :host_node, action)
    end
    done::Bool = false
    success = false

    if curr_node == nv(vnr) #we place all the virtual nodes successefully
        sn, vnr, success = solver(sn, vnr)
        # the simulation ends here, even if link placement fails
        done = true
    end
    reward::Float64 = calculateReward(sn, vnr, success)
    return sn, vnr, min(curr_node+1, nv(vnr)), reward, done
end
