def solution():
    # Calculate the total cost of the Ferris wheel ride for the 3 children
    ferris_wheel_cost = 3 * 5  # $5 per child, and only 3 children went on the ride

    # Calculate the total cost of the merry-go-round ride for all 5 children
    merry_go_round_cost = 5 * 3  # $3 per child, and all 5 children rode

    # Calculate the total cost of the ice cream cones for all 5 children
    ice_cream_cost = 2 * 8 * 5  # $8 per cone, and each child had 2 cones

    # Calculate the total amount spent altogether
    total_cost = ferris_wheel_cost + merry_go_round_cost + ice_cream_cost
    result = total_cost
    return result

print(solution())