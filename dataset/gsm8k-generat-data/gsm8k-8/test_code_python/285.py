def solution():
    # Calculate the total number of minutes in the show
    total_minutes = 20 * 30

    # Convert the total minutes to hours
    total_hours = total_minutes / 60

    # Calculate the hours needed per day to finish the show in 5 days
    hours_per_day = total_hours / 5
    result = hours_per_day
    return result

print(solution())