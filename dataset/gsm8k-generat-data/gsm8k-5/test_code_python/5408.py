def solution():
    peanuts_per_second = 20 / 15  # Darma eats 20 peanuts in 15 seconds

    # Calculate the total number of seconds in 6 minutes
    total_seconds = 6 * 60

    # Calculate the total number of peanuts Darma would eat in 6 minutes
    total_peanuts = peanuts_per_second * total_seconds
    result = total_peanuts
    return result

print(solution())