def solution():
    """A group of 5 children are taken to an amusement park. Only 3 of them were daring enough to get on the Ferris wheel which cost $5 per child. Everyone had a go at the merry-go-round (at $3 per child). On their way home, they bought 2 cones of ice cream each (each cone cost $8). How much did they spend altogether?"""
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