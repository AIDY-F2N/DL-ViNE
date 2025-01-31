include("utils.jl")


function place_links_dl(sn::MetaGraph{Int64, Float64}, vnr::MetaGraph{Int64, Float64})
    ed = collect(edges(vnr))
    v = sort(ed, by = e -> get_prop(vnr, e, :BW), rev = true)

    for e in v
        src_host = get_prop(vnr, e.src, :host_node)
        dst_host = get_prop(vnr, e.dst, :host_node)
        
        # Handle the case where src_host and dst_host are the same
        if src_host == dst_host
            # No need to place links if src_host and dst_host are the same node
            continue
        end
        
        p = direct_link(sn, src_host, dst_host, get_prop(vnr, e, :BW))
        if isempty(p)
            # Return empty graphs if no direct link is found
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

function direct_link(g::MetaGraph{Int64, Float64}, source::Int64, dest::Int64, threshold::Int64)
    if dest in neighbors(g, source)
        p = props(g, source, dest)
        if p[:BW_max] - p[:BW_used] >= threshold
            return [source, dest]
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


