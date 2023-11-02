def solution():
    num_children = 5
    num_daring = 3
    ferris_wheel_cost = 5
    merry_go_round_cost = 3
    ice_cream_cost = 8

    # Calculate the total cost of the Ferris wheel for the daring children
    ferris_wheel_total = num_daring * ferris_wheel_cost

    # Calculate the total cost of the merry-go-round for all children
    merry_go_round_total = num_children * merry_go_round_cost

    # Calculate the total cost of the ice cream cones for all children
    ice_cream_total = num_children * 2 * ice_cream_cost

    # Calculate the total cost of everything
    total_cost = ferris_wheel_total + merry_go_round_total + ice_cream_total
    result = total_cost
    return result

print(solution())