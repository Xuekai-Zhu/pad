def solution():
    # Calculate the total number of 20-minute periods during the 6-hour period
    total_periods = (7-1) * 3  # the Ferris wheel is open for 6 hours (from 1:00 pm to 7:00 pm), with 3 20-minute periods per hour

    # Calculate the total number of people who can ride during the 6-hour period
    total_capacity = 70 * total_periods

    result = total_capacity
    return result

print(solution())