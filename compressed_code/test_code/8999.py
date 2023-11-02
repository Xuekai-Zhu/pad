def solution():
    
    num_children = 5
    num_daring = 3
    ferris_wheel_cost = 5
    merry_go_round_cost = 3
    ice_cream_cost = 8
    num_ice_creams = 2
    total_ferris_wheel_cost = num_daring * ferris_wheel_cost
    total_merry_go_round_cost = num_children * merry_go_round_cost
    total_ice_cream_cost = num_children * num_ice_creams * ice_cream_cost
    total_cost = total_ferris_wheel_cost + total_merry_go_round_cost + total_ice_cream_cost
    result = total_cost
    return result

print(solution())