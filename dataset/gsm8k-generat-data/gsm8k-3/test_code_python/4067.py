def solution():
    """A group of 5 children are taken to an amusement park. Only 3 of them were daring enough to get on the Ferris wheel which cost $5 per child. Everyone had a go at the merry-go-round (at $3 per child). On their way home, they bought 2 cones of ice cream each (each cone cost $8). How much did they spend altogether?"""
    # Define the prices of each activity and item
    FERRIS_WHEEL_PRICE = 5
    MERRY_GO_ROUND_PRICE = 3
    ICE_CREAM_PRICE = 8

    # Define the number of children who participated in each activity/item
    ferris_wheel_children = 3
    merry_go_round_children = 5
    ice_cream_children = 5

    # Calculate the total cost of the Ferris wheel rides
    ferris_wheel_cost = ferris_wheel_children * FERRIS_WHEEL_PRICE

    # Calculate the total cost of the merry-go-round rides
    merry_go_round_cost = merry_go_round_children * MERRY_GO_ROUND_PRICE

    # Calculate the total cost of the ice cream cones
    ice_cream_cost = ice_cream_children * 2 * ICE_CREAM_PRICE

    # Calculate the total cost of all the activities/items
    total_cost = ferris_wheel_cost + merry_go_round_cost + ice_cream_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())