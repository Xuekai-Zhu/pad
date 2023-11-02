def solution():
    # Calculate the total number of minutes Ayen jogged during the weekdays
    total_minutes = 30 * 3  # 30 minutes per day, 3 weekdays

    # Add the extra minutes for Tuesday and Friday
    total_minutes += 5 + 25

    # Convert minutes to hours
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())