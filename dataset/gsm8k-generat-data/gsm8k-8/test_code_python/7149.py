def solution():
    # Define the cost of each daily newspaper
    daily_cost = 0.5

    # Calculate the total cost of the daily newspapers over 8 weeks
    daily_total_cost = daily_cost * 3 * 3 * 8

    # Define the cost of the Sunday newspaper
    sunday_cost = 2

    # Calculate the total cost of the Sunday newspaper over 8 weeks
    sunday_total_cost = sunday_cost * 8

    # Calculate the total cost of all the newspapers over 8 weeks
    total_cost = daily_total_cost + sunday_total_cost
    result = total_cost
    return result

print(solution())