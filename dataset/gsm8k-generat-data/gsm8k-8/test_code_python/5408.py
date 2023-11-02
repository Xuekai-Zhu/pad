def solution():
    # Define the number of seconds in 6 minutes
    minutes_to_seconds = 6 * 60

    # Calculate the number of peanuts Darma can eat in 1 second
    peanuts_per_second = 20 / 15

    # Calculate the total number of peanuts Darma can eat in 6 minutes
    total_peanuts = peanuts_per_second * minutes_to_seconds
    result = total_peanuts
    return result

print(solution())