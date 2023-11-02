def solution():
    """Sarah is buying Christmas presents for her family. She starts her shopping with a certain amount of money. She buys 2 toy cars for $11 each for her sons. She buys a scarf for $10 for her mother. Then she buys a beanie for $14 for her brother. If she has $7 remaining after purchasing the beanie, how much money did she start with?"""
    # Define the cost of each item
    TOY_CAR_COST = 11
    SCARF_COST = 10
    BEANIE_COST = 14

    # Define the number of each item purchased
    num_toy_cars = 2

    # Calculate the total cost of the toy cars
    toy_car_cost = num_toy_cars * TOY_CAR_COST

    # Calculate the total cost of all items except for the beanie
    non_beanie_cost = toy_car_cost + SCARF_COST

    # Calculate the starting amount of money
    starting_money = non_beanie_cost + BEANIE_COST + 7

    # Display the starting amount of money
    result = starting_money
    return result

print(solution())