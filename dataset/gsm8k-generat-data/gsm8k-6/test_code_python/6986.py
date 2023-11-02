def solution():
    # Calculate the total distance Briar travels per day
    daily_distance = 2 * 200  # Briar goes to the event and back home every day

    # Calculate the total distance Briar travels in one week
    weekly_distance = daily_distance * 7  # Briar attends the event for one week

    # Calculate the total cost of the cab rides
    cab_cost = weekly_distance * 2.5  # A cab ride costs $2.5 per mile

    result = cab_cost
    return result

print(solution())