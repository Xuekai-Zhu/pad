def solution():
    # Calculate the total number of minutes Carolyn practices each day
    total_minutes = 20 + 3 * 20  # Carolyn practices the piano for 20 minutes and the violin for three times as long

    # Calculate the total number of minutes Carolyn practices in a week
    weekly_minutes = total_minutes * 6  # Carolyn practices for six days a week

    # Calculate the total number of minutes Carolyn practices in a month
    monthly_minutes = weekly_minutes * 4  # There are four weeks in a month

    result = monthly_minutes
    return result

print(solution())