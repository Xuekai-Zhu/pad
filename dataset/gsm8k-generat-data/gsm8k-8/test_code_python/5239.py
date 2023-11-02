def solution():
    # Calculate the total number of peanuts
    total_peanuts = 4 * 30

    # Calculate the total time in minutes
    total_time_minutes = 2 * 60

    # Calculate the time between eating each peanut
    time_between_peanuts = total_time_minutes / (total_peanuts - 1)

    result = time_between_peanuts
    return result

print(solution())