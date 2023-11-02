def solution():
    # Define the starting number of cans and the increase per day
    starting_cans = 20
    increase_per_day = 5

    # Define the number of days they collected and calculate the total increase in cans
    num_days = 5
    total_increase = increase_per_day * (num_days - 1)

    # Calculate the total cans collected by adding the starting amount and the increase
    total_cans = starting_cans + total_increase

    # Divide the total by the number of days to find the goal per week
    goal_per_week = total_cans / num_days
    result = goal_per_week
    return result

print(solution())