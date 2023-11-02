def solution():
    """A group of 5 children are taken to an amusement park. Only 3 of them were daring enough to get on the Ferris wheel which cost $5 per child. Everyone had a go at the merry-go-round (at $3 per child). On their way home, they bought 2 cones of ice cream each (each cone cost $8). How much did they spend altogether?"""
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