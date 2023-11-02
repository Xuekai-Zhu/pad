def solution():
    hourly_rate = 9  # Olivia earns $9 per hour
    monday_hours = 4
    wednesday_hours = 3
    friday_hours = 6

    # Calculate the total money Olivia earned
    total_earned = hourly_rate * (monday_hours + wednesday_hours + friday_hours)
    result = total_earned
    return result

print(solution())