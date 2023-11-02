def solution():
    # Calculate the number of surfers on the second and third day
    surfers_second_day = 1500 + 600
    surfers_third_day = 2/5 * 1500

    # Calculate the total number of surfers for the three days
    total_surfers = 1500 + surfers_second_day + surfers_third_day

    # Calculate the average number of surfers per day
    average_surfers = total_surfers / 3
    result = average_surfers
    return result

print(solution())