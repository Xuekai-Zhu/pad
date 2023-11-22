def solution():
    
    # Define the cost of a single banana and a bunch
    banana_cost = 0.8
    bunch_cost = 3.0

    # Calculate the total cost of buying 10 bunches of bananas
    bunch_total_cost = 10 * 4 * banana_cost

    # Calculate the total cost of buying 10 bunches of bananas
    total_cost = 10 * bunch_cost

    # Calculate the savings by buying in bunches instead of individually
    savings = total_cost - banana_cost

    # return the result
    result = savings
    return result

print(solution())