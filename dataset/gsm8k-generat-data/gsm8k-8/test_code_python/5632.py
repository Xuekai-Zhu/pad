def solution():
    # Calculate total minutes of the show
    total_minutes = 90 * 20

    # Convert two hours to minutes
    daily_minutes = 2 * 60

    # Calculate how many days it will take to finish watching the show
    days_to_finish = total_minutes / daily_minutes

    result = days_to_finish
    return result

print(solution())