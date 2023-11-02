def solution():
    # Define the number of sandwiches and the cost of drinks
    num_sandwiches = 3
    drink_cost = 4

    # Calculate the total cost of drinks
    total_drink_cost = drink_cost * 2

    # Calculate the remaining cost after buying drinks
    remaining_cost = 26 - total_drink_cost

    # Divide the remaining cost evenly among the three sandwiches
    sandwich_cost = remaining_cost / num_sandwiches
    result = sandwich_cost
    return result

print(solution())