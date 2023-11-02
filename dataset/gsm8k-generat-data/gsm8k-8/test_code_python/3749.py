def solution():
    # Define the given values
    servings_per_container = 6
    servings_per_day = 3
    container_duration_in_days = servings_per_container / (servings_per_day * 0.5)
    weeks = 2
    total_days = weeks * 7
    number_of_containers = total_days / container_duration_in_days
    cost_per_container = 3.00

    # Calculate the total cost
    total_cost = number_of_containers * cost_per_container
    result = total_cost
    return result

print(solution())