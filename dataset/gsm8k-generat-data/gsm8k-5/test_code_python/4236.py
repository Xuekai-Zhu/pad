def solution():
    time_played = 3  # John played at the arcade for 3 hours
    cost_per_minute = 0.5 / 6  # John spends $0.50 for every 6 minutes

    # Calculate the total cost
    total_cost = time_played * 60 * cost_per_minute

    result = total_cost
    return result

print(solution())