function check_bounds_are_respected(sn)
    used = []
    for n in 1:nv(sn)
        @assert 0 <= get_prop(sn, n, :cpu_used) <= get_prop(sn, n, :cpu_max)
    end
    for e in edges(sn)
        @assert 0 <= get_prop(sn, e, :BW_used) <= get_prop(sn, e, :BW_max)
    end
end 


function check_each_vn_uses_resource_amount(sn, vnr)
    # Dictionary to store CPU usage per host
    cpu_usage_per_host = Dict{Any, Int}()

    # Iterate over each virtual pod
    for n in 1:nv(vnr)
        host = get_prop(vnr, n, :host_node)
        cpu = get_prop(vnr, n, :cpu)
        cpusn=get_prop(sn, host, :cpu_max)
        # Update CPU usage for the current host
        cpu_usage_per_host[host] = get(cpu_usage_per_host, host, 0) + cpu

        # Check CPU usage for the current host against the previous snapshot
        @assert cpu_usage_per_host[host] <= get_prop(sn, host, :cpu_max)
        cmax=get_prop(sn, host, :cpu_max)
        cused=get_prop(sn, host, :cpu_used)
    end
end

function check_each_vl_uses_resource_amount(sn, sn_prec, vnr)  
    vlink_cons = Dict()
    used_edges::Int64=0
    for e in edges(vnr)
        src=get_prop(vnr, e.src, :host_node)
        dst=get_prop(vnr, e.dst, :host_node)
        vlink = get_prop(vnr, e, :vlink)
        for (l, bw) in vlink
            @assert l[1]==src
            @assert l[2]==dst
            used_edges+=1
            if l[1] > l[2]
                l = (l[2], l[1])
            end
            if !haskey(vlink_cons, l)
                vlink_cons[l] = 0
            end
            vlink_cons[l] += bw
        end
    end
    for e in edges(sn)
        u = e.src
        v = e.dst
        if u < v
            l = (u, v)
        else
            l = (v, u)
        end
        if haskey(vlink_cons, (u, v))
            @assert vlink_cons[(u, v)] == get_prop(sn, u, v, :BW_used) - get_prop(sn_prec, u, v, :BW_used) 
        elseif haskey(vlink_cons, (v, u))
            @assert vlink_cons[(u, v)] == get_prop(sn, u, v, :BW_used) - get_prop(sn_prec, u, v, :BW_used)
        else
            @assert 0 == get_prop(sn, u, v, :BW_used) - get_prop(sn_prec, u, v, :BW_used) 
        end
    end
end

#For NEPA
function check_each_vl_uses_resource_amount_nepa(sn, sn_prec, vnr)  
    vlink_cons = Dict()
    for e in edges(vnr)
        vlink = get_prop(vnr, e, :vlink)
        for (l, bw) in vlink
            if l[1] > l[2]
                l = (l[2], l[1])
            end
            if !haskey(vlink_cons, l)
                vlink_cons[l] = 0
            end
            vlink_cons[l] += bw
        end
    end
    for e in edges(sn)
        u = e.src
        v = e.dst
        if u < v
            l = (u, v)
        else
            l = (v, u)
        end
        if haskey(vlink_cons, (u, v))
            @assert vlink_cons[(u, v)] == get_prop(sn, u, v, :BW_used) - get_prop(sn_prec, u, v, :BW_used) 
        elseif haskey(vlink_cons, (v, u))
            @assert vlink_cons[(u, v)] == get_prop(sn, u, v, :BW_used) - get_prop(sn_prec, u, v, :BW_used)
        else
            @assert 0 == get_prop(sn, u, v, :BW_used) - get_prop(sn_prec, u, v, :BW_used) 
        end
    end
end