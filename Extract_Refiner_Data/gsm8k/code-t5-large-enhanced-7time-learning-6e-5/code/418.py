def solution():
    
    # Define the initial cost of the service
    initial_cost = 8 * 6

    # Define the cost of the service after the first 6 months
    final_cost = 12 * 8

    # Define the cost of the service after 8 months
    final_cost += 14 * 8

    # Calculate the total cost for 2 years
    total_cost = final_cost * 2

    # return the result
    result = total_cost
    return result

print(solution())