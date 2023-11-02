def solution():
    # Define the cost of the baguettes and water
    baguette_cost = 2
    water_cost = 1

    # Calculate the total cost of the baguettes and water
    total_cost = (2 * baguette_cost) + (2 * water_cost)

    # Calculate the amount of money Kenneth has left
    money_left = 50 - total_cost
    result = money_left
    return result

print(solution())