def solution():
    # Calculate the total number of hours needed to read the bible
    total_hours = 2800 / 50 / 2  # read at a rate of 50 pages an hour and for 2 hours a day
    weeks = total_hours / 7  # Assuming John reads every day of the week
    result = weeks
    return result

print(solution())