def solution():
    cost_ferris_wheel = 5
    cost_merry_go_round = 3
    cost_ice_cream_cone = 8
    children_on_ferris_wheel = 3
    children_on_merry_go_round = 5
    children_buying_ice_cream = 5
    total_children = children_on_ferris_wheel + children_on_merry_go_round + children_buying_ice_cream
    total_cost = cost_ferris_wheel * children_on_ferris_wheel + cost_merry_go_round * children_on_merry_go_round + cost_ice_cream_cone * children_buying_ice_cream
    result = total_cost
    
    return result

print(solution())