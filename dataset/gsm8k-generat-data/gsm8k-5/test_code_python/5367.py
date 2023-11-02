def solution():
    total_balloons = 52  # Kate needs to fill 52 balloons
    air_per_balloon = 5  # Each balloon holds 5 gallons of air

    # Calculate the total amount of air needed
    total_air = total_balloons * air_per_balloon

    # Calculate the time taken to fill the first 10 balloons
    time_first_10 = 10  # Kate fills the first 10 balloons at a rate of 8 gallons per minute
    air_first_10 = time_first_10 * 8

    # Calculate the time taken to fill the next 10 balloons
    time_next_10 = 5  # Kate fills the next 10 balloons at a rate of 4 gallons per minute
    air_next_10 = time_next_10 * 4

    # Calculate the time taken to fill the remaining balloons
    air_remaining = total_air - air_first_10 - air_next_10
    time_remaining = air_remaining / 2

    # Calculate the total time taken
    total_time = time_first_10 + time_next_10 + time_remaining
    result = total_time
    return result

print(solution())