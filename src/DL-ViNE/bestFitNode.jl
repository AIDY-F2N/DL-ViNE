function bestFitNode(m, vn, vnr, sn)
    vn_edges = []
    vn_edges=get_vn_egdes(vn, vnr)
    total=0
    good=0
    free_bw= Dict{Int, Int}()
    for e in vn_edges 
        BW=get_prop(vnr, e, :BW)
        if has_prop(vnr, e.src, :host_node) || has_prop(vnr, e.dst, :host_node)
            known_host=0
            try
                if e.src == vn
                    known_host = get_prop(vnr, e.dst, :host_node)     
                else
                    known_host = get_prop(vnr, e.src, :host_node)
                end
            catch
                continue
            end
            
            if known_host != 0
                total+=1
                if m != known_host                    
                    neighborsList = Set{Int64}()
                    for neighbor in neighbors(sn, known_host)
                        push!(neighborsList, neighbor)
                    end
                    neighborsList = collect(neighborsList)
                    for neighbor in neighborsList
                        if neighbor==m 
                            one=true
                            if has_prop(sn, m, known_host, :BW_max)
                                available_BW = get_prop(sn, m, known_host, :BW_max) - get_prop(sn, m, known_host, :BW_used)
                            else 
                                one=false
                                available_BW = get_prop(sn,known_host, m, :BW_max) - get_prop(sn, known_host,m, :BW_used)
                            end
                            
                            if available_BW >= BW 
                                good+=1
                                if haskey(free_bw, known_host)
                                    free_bw[known_host]=+BW
                                else 
                                    free_bw[known_host]=BW
                                end
                                if one == true
                                    set_prop!(sn, m, known_host, :BW_used, get_prop(sn, known_host,m, :BW_used)+BW)
                                else
                                    set_prop!(sn, known_host, m, :BW_used, get_prop(sn, known_host,m, :BW_used)+BW)
                                end 
                            end
                        end
                    end
                else
                    good+=1 #if m == known_host 
                end
            end
        end
    end
    #free BW
    for (host, BW) in free_bw
        if has_prop(sn, m, host, :BW_max)
            set_prop!(sn, m, host, :BW_used, get_prop(sn, host, m, :BW_used)-BW)
        else 
            set_prop!(sn, host, m, :BW_used, get_prop(sn, host, m, :BW_used)-BW)
        end
    end

    if total>0 && total==good
        return true
    else 
       return false
    end
end

function get_vn_egdes(vn, vnr)
    ed = collect(edges(vnr))
    vn_edges = []
    for e in ed
        if e.src == vn || e.dst == vn
            push!(vn_edges, e)
        end
    end
    return vn_edges
end

function has_prop(graph, node, prop)
    try
        get_prop(graph, node, prop)
        return true
    catch
        return false
    end
end

function has_prop(graph, node, node2, prop)
    try
        get_prop(graph, node,node2, prop)
        return true
    catch
        return false
    end
end
