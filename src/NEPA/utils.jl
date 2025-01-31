import Base.parse
import Base.isempty
import Base.push!
import Base.popfirst!
########################################################
############### FILE LOADING FUNCTIONS #################
########################################################

function parse(T::Type{Int64}, a::Int64)
    return a
end

function load_sn(filename::String)
    json_graph = JSON.parsefile(filename)
    g = MetaGraph(json_graph["n"]);
    
    for i = 1:json_graph["n"]
        set_prop!(g, i, :cpu_max, json_graph["nodes_cap"][string(i-1)]::Int64)
        set_prop!(g, i, :cpu_used, 0::Int64) 
    end
    
    for edge in json_graph["edges"]
        add_edge!(g, parse(Int64, edge["e"][1])+1::Int64, parse(Int64, edge["e"][2])+1::Int64)
        set_prop!(g, parse(Int64, edge["e"][1])+1::Int64, parse(Int64, edge["e"][2])+1::Int64, :BW_max, edge["weight"]::Int64)
        set_prop!(g, parse(Int64, edge["e"][1])+1::Int64, parse(Int64, edge["e"][2])+1::Int64, :BW_used, 0::Int64)
    end

    return g
end

function load_vnr(filename::String)
    json_graph = JSON.parsefile(filename)
    g = MetaGraph(json_graph["n"]);
    
    #if !order_nodes
    perm = 1:json_graph["n"]

    for i in perm
        set_prop!(g, i, :cpu, json_graph["nodes_cap"][string(i-1)]::Int64)
    end

    for edge in json_graph["edges"]
        add_edge!(g, edge["e"][1]+1::Int64, edge["e"][2]+1::Int64)
        set_prop!(g, edge["e"][1]+1::Int64, edge["e"][2]+1::Int64, :BW, edge["weight"]::Int64)
        set_prop!(g, edge["e"][1]+1::Int64, edge["e"][2]+1::Int64, :vlink, Dict{Tuple{Int64, Int64}, Float64}())
    end
    return g
end

function load_instance(file_path::String)
    # element -1 is our physical network, then it is slice 0, 1, 2, ...
    instance = Dict{Int64, MetaGraph{Int64,Float64}}()
    events = []
    for (i,l) in enumerate(eachline(file_path * "/events.txt"))
        if i != 1
            l = replace(l, "\'" => "\"")
            T = eval(Meta.parse(l))
            push!(events, (T[2], T[3]))
        end
    end
    for f in readdir(file_path)
        if SubString(f, 1, 5) == "slice"
            n = split(f," ")[end]
            number = parse(Int64, n)
            instance[number] = load_vnr(file_path * "/" * f)
        end
    end
    instance[-1] = load_sn(file_path * "/test_network")
    return events, instance
end

function calculateReward(sn, vnr, success)
    if success
        used_resources::Float64 = 0
        asked_resources::Float64 = 0

        for (i, e) in enumerate(edges(vnr))
            p = props(vnr, e)
            asked_resources += p[:BW]
            vlink::Dict{Tuple{Int64, Int64}, Float64} = p[:vlink]
            for (k, v) in vlink
                used_resources += v
            end
        end
        for (i, v) in enumerate(vertices(vnr))
            p = props(vnr, v)
            used_resources += p[:cpu]
            asked_resources += p[:cpu]
        end
        return asked_resources / used_resources
    else
        return 0
    end
end


# copying graphs with copy() is painfully slow, better to copy by hand
function copy_graph(gr::MetaGraph{Int64, Float64})
    g = MetaGraph(nv(gr));
     for i = 1:nv(gr)
        p = props(gr, i)
        # we do not copy directly from p since it is passed by reference
        set_props!(g, i, copy(p))
    end
    
    for edge in edges(gr)
        e = props(gr, edge)
        add_edge!(g, edge)
        set_props!(g, edge, copy(e))
    end
    return g
end

function copy_graph!(source::MetaGraph{Int64, Float64}, dest::MetaGraph{Int64, Float64})
    for i = 1:nv(source)
        p = props(source, i)
        # we do not copy directly from p since it is passed by reference
        set_props!(dest, i, copy(p))
    end
    
    for edge in edges(source)
        e = props(source, edge)
        add_edge!(dest, edge)
        set_props!(dest, edge, copy(e))
    end
end

function get_legal_moves(sn::MetaGraph{Int64, Float64}, vnr::MetaGraph{Int64, Float64}, curr_node::Int64, bws_sn, bws_vnr, sum_bws_sn, sum_bws_vnr)
    legal_moves = []
     for i in 1:nv(sn)
        p = props(sn, i)
        if p[:cpu_max] - p[:cpu_used] > get_prop(vnr, curr_node, :cpu) && bws_sn[i] >= bws_vnr[curr_node] && sum_bws_sn[i] >= sum_bws_vnr[curr_node]
            push!(legal_moves, i)
        end
    end
    return legal_moves
end

function get_legal_moves(sn::MetaGraph{Int64, Float64}, vnr::MetaGraph{Int64, Float64}, curr_node::Int64)
    #if haskey(known_legals::Dict{String, Vector{Int64}}, key)
    #    println(1)
    #    return known_legals[key]
    #end
    legal_moves = []
     for i in 1:nv(sn)
        p = props(sn, i)
        if p[:cpu_max] - p[:cpu_used] > get_prop(vnr, curr_node, :cpu) # && bws_sn[i] >= bws_vnr[curr_node] && sum_bws_sn[i] >= sum_bws_vnr[curr_node]
            push!(legal_moves, i)
        end
    end
    #known_legals[key] = legal_moves
    #println(0)
    return legal_moves
end

function remove!(a, item)
    if issubset([item], a)
        deleteat!(a, findfirst(x->x==item, a))
    end
end


function max_bw_sn(sn)
    bws = []
    for i in 1:nv(sn)
        max_bw = 0
        for n in neighbors(sn, i)
            if get_prop(sn, i, n, :BW_max) - get_prop(sn, i, n, :BW_used) > max_bw
                max_bw = get_prop(sn, i, n, :BW_max) - get_prop(sn, i, n, :BW_used)
            end
        end
        push!(bws, max_bw)
    end
    return bws
end

function max_bw_vnr(vnr)
    bws = []
    for i in 1:nv(vnr)
        max_bw = 0
        for n in neighbors(vnr, i)
            if get_prop(vnr, i, n, :BW) > max_bw
                max_bw = get_prop(vnr, i, n, :BW)
            end
        end
        push!(bws, max_bw)
    end
    return bws
end

function sum_bw_sn(sn)
    bws = []
    for i in 1:nv(sn)
        sum_bw = 0
        for n in neighbors(sn, i)
            sum_bw += get_prop(sn, i, n, :BW_max) - get_prop(sn, i, n, :BW_used)
        end
        push!(bws, sum_bw)
    end
    return bws
end

function sum_bw_vnr(vnr)
    bws = []
    for i in 1:nv(vnr)
        sum_bw = 0
        for n in neighbors(vnr, i)
            sum_bw += get_prop(vnr, i, n, :BW)
        end
        push!(bws, sum_bw)
    end
    return bws
end

# sort by ascending order of number of candidates
function reorder_vnr(vnr, sn, max_bw_sn, max_bw_vnr, sum_bw_sn, sum_bw_vnr)
    num_candidates = []
    vnr_reordered = MetaGraph(nv(vnr))
    for i in 1:nv(vnr)
        push!(num_candidates, length(get_legal_moves(sn, vnr, i, max_bw_sn, max_bw_vnr, sum_bw_sn, sum_bw_vnr)))
    end
    indexes = sortperm(num_candidates)
    #println(indexes)
    for i in 1:nv(vnr)
        set_prop!(vnr_reordered, i, :cpu, get_prop(vnr, indexes[i], :cpu))
    end
    for e in edges(vnr)
        add_edge!(vnr_reordered, indexes[e.src], indexes[e.dst])
        set_prop!(vnr_reordered, indexes[e.src], indexes[e.dst], :BW, get_prop(vnr, e.src, e.dst, :BW))
        set_prop!(vnr_reordered, indexes[e.src], indexes[e.dst], :vlink, Dict{Tuple{Int64, Int64}, Float64}())
    end
    return vnr_reordered
end


function get_rtc(scores, accepted)
    glob_r_c = 0
    for (size, l) in scores
        for i in l
            if i > 0
                glob_r_c += i
            end
        end
    end
    glob_r_c /= accepted

    return glob_r_c
end

struct ThreadQueue{T,N<:Integer}
    data::Vector{T}
    head::Threads.Atomic{N} #Index of the head
    tail::Threads.Atomic{N} #Index of the tail
end

function ThreadQueue(T::Type, maxlength::N) where N <: Integer
    q = ThreadQueue(Vector{T}(undef, maxlength), Threads.Atomic{N}(1), Threads.Atomic{N}(1))
    return q
end

function push!(q::ThreadQueue{T,N}, val::T) where T where N
    # TODO: check that head > tail
    offset = Threads.atomic_add!(q.tail, one(N))
    q.data[offset] = val
    return offset
end

function popfirst!(q::ThreadQueue{T,N}) where T where N
    # TODO: check that head < tail
    offset = Threads.atomic_add!(q.head, one(N))
    return q.data[offset]
end

function isempty(q::ThreadQueue{T,N}) where T where N
    return (q.head[] == q.tail[]) && q.head != one(N)
end

function getindex(q::ThreadQueue{T}, iter) where T
    return q.data[iter]
end

function precompute_distances(sn, threshold)
    sn2 = copy_graph(sn)
    for e in edges(sn)
        p = props(sn, e)
        if p[:BW_max] - p[:BW_used] < threshold
            rem_edge!(sn2, e)
        end
    end
    distances = []
     for node in 1:nv(sn2)
        push!(distances, gdistances(sn2, node))
    end
    return distances 
end


function default_weight!(policy, key)
    policy[key] = 0
end

function default_weight!(policy, key, distances)
    if distances == nothing
        policy[key] = 0
        return
    end
    if key == ""
        policy[key] = 0
    else
        nodes = split(key, ",")
        k = 0
        # first "node" is always empty string, last one is the node we are trying to rate
         for i in nodes[2:end-1]
            k += distances[parse(Int64, nodes[end])][parse(Int64, i)]
        end
        policy[key] = -k / (length(nodes)-1)
    end
end


function median_bw(vnr)
    a = []
    for e in edges(vnr)
        push!(a, get_prop(vnr, e, :BW))
    end
    return median(a)
end 
