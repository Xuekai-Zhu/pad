def solution():
    num_balloons = 52
    air_per_balloon = 5

    rate_1_time = 10
    rate_1 = 8

    rate_2_time = 5
    rate_2 = rate_1 / 2

    rate_3 = 2

    # Calculate the total amount of air needed to fill all of the balloons
    total_air = num_balloons * air_per_balloon

    # Calculate the time it takes to fill the balloons with the first rate
    time_1 = rate_1_time * rate_1

    # Calculate the time it takes to fill the balloons with the second rate
    time_2 = rate_2_time * rate_2

    # Calculate the remaining amount of air that needs to be filled with the third rate
    remaining_air = total_air - (rate_1_time * rate_1 * air_per_balloon) - (
                rate_2_time * rate_2 * air_per_balloon)

    # Calculate the time it takes to fill the remaining balloons with the third rate
    time_3 = (remaining_air / rate_3)

    # Calculate the total time it takes to fill all of the balloons
    total_time = time_1 + time_2 + time_3
    result = total_time
    return result

print(solution())