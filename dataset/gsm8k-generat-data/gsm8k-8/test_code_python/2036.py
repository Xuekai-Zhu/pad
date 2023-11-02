def solution():
    # Calculate the number of days Mr. Johnson has taken pills
    days_taken = 30 * (4/5)

    # Calculate the number of pills Mr. Johnson has taken
    pills_taken = 30 - days_taken

    # Calculate the number of pills Mr. Johnson should take per day
    pills_per_day = pills_taken / days_taken
    result = pills_per_day
    return result

print(solution())