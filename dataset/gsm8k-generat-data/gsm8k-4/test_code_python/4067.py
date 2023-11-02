def solution():
    """A group of 5 children are taken to an amusement park. Only 3 of them were daring enough to get on the Ferris wheel which cost $5 per child. Everyone had a go at the merry-go-round (at $3 per child). On their way home, they bought 2 cones of ice cream each (each cone cost $8). How much did they spend altogether?"""
    # Define the number of children and the cost of each ride
    CHILDREN = 5
    FERRIS_WHEEL_COST = 5
    MERRY_GO_ROUND_COST = 3
    ICE_CREAM_COST = 8

    # Calculate the total cost of the Ferris wheel ride
    ferris_wheel_cost = 3 * FERRIS_WHEEL_COST

    # Calculate the total cost of the merry-go-round ride
    merry_go_round_cost = CHILDREN * MERRY_GO_ROUND_COST

    # Calculate the total cost of the ice cream cones
    ice_cream_cost = CHILDREN * 2 * ICE_CREAM_COST

    # Calculate the total spending
    total_spending = ferris_wheel_cost + merry_go_round_cost + ice_cream_cost

    # Return the result
    result = total_spending
    return result

print(solution())