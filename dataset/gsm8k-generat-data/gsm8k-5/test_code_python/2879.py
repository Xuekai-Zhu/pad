def solution():
    minutes_per_day = 2 * 3  # Malcolm brushes his teeth 3 times a day for 2 minutes each time
    days = 30  # Malcolm brushes his teeth for 30 days

    # Calculate the total time Malcolm spends brushing his teeth
    total_minutes = minutes_per_day * days
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())