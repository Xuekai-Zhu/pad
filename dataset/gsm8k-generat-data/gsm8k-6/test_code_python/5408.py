def solution():
    # Calculate the number of peanuts Darma can eat in 1 second
    peanuts_per_second = 20 / 15

    # Calculate the number of peanuts Darma can eat in 1 minute
    peanuts_per_minute = peanuts_per_second * 60

    # Calculate the number of peanuts Darma can eat in 6 minutes
    peanuts_in_6_minutes = peanuts_per_minute * 6

    result = peanuts_in_6_minutes
    return result

print(solution())