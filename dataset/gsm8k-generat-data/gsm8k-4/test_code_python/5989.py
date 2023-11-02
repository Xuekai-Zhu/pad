def solution():
    """Sarah is buying Christmas presents for her family. She starts her shopping with a certain amount of money. She buys 2 toy cars for $11 each for her sons. She buys a scarf for $10 for her mother. Then she buys a beanie for $14 for her brother. If she has $7 remaining after purchasing the beanie, how much money did she start with?"""
    # Define the cost of each present
    toy_car_cost = 11
    scarf_cost = 10
    beanie_cost = 14

    # Define the number of each present purchased
    toy_car_count = 2

    # Calculate the total cost of all presents
    total_cost = (toy_car_cost * toy_car_count) + scarf_cost + beanie_cost + 7

    # Calculate the initial amount of money Sarah started with
    initial_amount = total_cost

    # return the result
    result = initial_amount
    return result

print(solution())