include("utils.jl")


function adapt(policy, sequence, sn, vnr, distances, solver::Function, max_bw_sn, max_bw_vnr, sum_bw_sn, sum_bw_vnr)
    polp = copy(policy)
    key = ""
    alpha::Float64 = 1
    curr_node = 1
     for action in sequence
        key *= ","
        key *= string(action)
        if !haskey(polp, key)
            default_weight!(polp, key, distances)
        end
        polp[key] += alpha
        z::Float64 = 0
        moves = get_legal_moves(sn, vnr, curr_node, max_bw_sn, max_bw_vnr, sum_bw_sn, sum_bw_vnr)
        for m in moves
            key_child = key * "," * string(m)
            if !haskey(policy, key_child)
                default_weight!(policy, key_child, distances)
            end
            z += exp(policy[key_child])
        end
        for m in moves
            key_child = key * "," * string(m)
            if !haskey(polp, key_child)
                default_weight!(polp, key_child, distances)
            end
            polp[key_child] -= alpha * (exp(policy[key_child]) / z)
        end
        # we avoid doing the last call to place links as it is expensive and we do not need the reward here
        # legal nodes are all that matters
        if curr_node < nv(vnr)
            sn, vnr, curr_node, reward::Float64, done::Bool = play(sn, vnr, curr_node, action, solver)
        end
    end
    return polp
end
