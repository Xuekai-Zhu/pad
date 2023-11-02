def solution():
    # Find the number of days Mr. Johnson has already taken pills
    days_taken = 30 * (4/5)

    # Find the number of pills he has taken so far
    pills_taken = 30 - days_taken

    # Find the average number of pills he takes per day
    pills_per_day = pills_taken / (30 - days_taken)

    result = pills_per_day
    return result

print(solution())