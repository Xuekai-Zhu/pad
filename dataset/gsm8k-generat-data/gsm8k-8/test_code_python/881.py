def solution():
    # Define the number of weeks and hours spent in the theater per week
    num_weeks = 6
    hours_per_week = 3

    # Calculate the total number of hours spent in the theater
    total_hours = num_weeks * hours_per_week

    # Calculate the total cost of tickets
    total_cost = total_hours * 5

    result = total_cost
    return result

print(solution())