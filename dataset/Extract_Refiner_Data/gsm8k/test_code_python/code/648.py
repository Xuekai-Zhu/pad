def solution():
    
    # Define the cost of the first paid hour and the cost of the remaining hours
    first_hour_cost = 15
    remaining_hours = 8
    remaining_cost = 2 * first_hour_cost

    # Calculate the total cost of the carriage
    total_cost = first_hour_cost + (remaining_hours * remaining_cost)

    # Display the total cost
    result = total_cost
    return result

print(solution())