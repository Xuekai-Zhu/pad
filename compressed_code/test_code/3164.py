def solution():
    
    ferris_wheel_cost = 5
    merry_go_round_cost = 3
    ice_cream_cost = 8
    num_children = 5
    num_daring_children = 3
    ferris_wheel_total = ferris_wheel_cost * num_daring_children
    merry_go_round_total = merry_go_round_cost * num_children
    ice_cream_total = ice_cream_cost * num_children * 2
    total_spent = ferris_wheel_total + merry_go_round_total + ice_cream_total
    result = total_spent
    return result

print(solution())