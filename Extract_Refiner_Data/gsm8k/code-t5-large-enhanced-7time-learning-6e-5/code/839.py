def solution():
    
    # Define the initial amount of money
    initial_money = 2 * 20

    # Define the cost of the squirt guns and the water balloons
    squirt_cost = 6 * 2
    water_cost = 3 * 3

    # Calculate the total cost of the items
    total_cost = squirt_cost + water_cost

    # Calculate the remaining money
    remaining_money = initial_money - total_cost

    # return the result
    result = remaining_money
    return result

print(solution())