def solution():
    
    # Define the time it takes to run the horse and the cost of a single bail of hay
    time_in_minutes = 30 * 60
    cost_per_bail = 3

    # Calculate the number of bags of hay Michael eats
    bags_of_hay = time_in_minutes // 2

    # Calculate the total cost of the hay
    total_cost = bags_of_hay * cost_per_bail

    # Calculate the amount of change Michael has after buying the hay
    change = 6 * 5 - total_cost

    # Display the amount of change
    result = change
    return result

print(solution())