include("utils.jl")


function direct_link(g::MetaGraph{Int64, Float64}, start::Int64, finish::Int64, threshold::Int64)
    if finish in neighbors(g, start)
        p = props(g, start, finish)
        if p[:BW_max] - p[:BW_used] >= threshold
            return [start, finish]
        end 
    end
    return Int64[]  # No direct edge found
end


function link_to_dict(p::Vector{Int64}, BW::Int64)
    d = Dict{Tuple{Int64, Int64}, Int64}()
    for i in 1:length(p)-1
        d[(p[i],p[i+1])] = BW
    end
    return d
end
 
function place_links_dl(sn::MetaGraph{Int64, Float64}, vnr::MetaGraph{Int64, Float64})
    ed = collect(edges(vnr))

    for e in ed
        src_host = get_prop(vnr, e.src, :host_node)
        dst_host = get_prop(vnr, e.dst, :host_node)
        
        # Handle the case where src_host and dst_host are the same
        if src_host == dst_host
            # No need to place links if src_host and dst_host are the same node    
            d=Dict{Tuple{Int64, Int64}, Float64}()
            d[(src_host,dst_host)] =0
            set_prop!(vnr, e, :vlink, d)
            continue
        end
        
        p = direct_link(sn, src_host, dst_host, get_prop(vnr, e, :BW))
        if isempty(p)
            # Return empty graphs if no path is found
            return MetaGraph{Int64, Float64}(), MetaGraph{Int64, Float64}(), false
        end
        for j = 1:length(p)-1
            u = p[j]
            v = p[j+1]
            set_prop!(sn, u, v, :BW_used, get_prop(sn, u, v, :BW_used) + get_prop(vnr, e, :BW))
        end
        
        d::Dict{Tuple{Int64, Int64}, Float64} = link_to_dict(p, get_prop(vnr, e, :BW))
        set_prop!(vnr, e, :vlink, d)
    end
    return sn, vnr, true
end


