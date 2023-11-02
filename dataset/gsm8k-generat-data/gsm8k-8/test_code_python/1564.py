def solution():
    # Calculate the total minutes of TV show watched for the week
    total_minutes = 8 * 44

    # Subtract the minutes watched on Monday, Thursday, and Friday
    total_minutes -= 138
    total_minutes -= 21
    total_minutes -= 2 * 44

    # Divide the remaining minutes over the weekend
    weekend_minutes = total_minutes / 2
    result = weekend_minutes
    return result

print(solution())