def solution():
    # Calculate the number of surfers on the second day
    surfers_on_second_day = 1500 + 600

    # Calculate the number of surfers on the third day
    surfers_on_third_day = 2 * (1500 / 5)

    # Calculate the total number of surfers for the three days
    total_surfers = 1500 + surfers_on_second_day + surfers_on_third_day

    # Calculate the average number of surfers for the three days
    average_surfers = total_surfers / 3

    result = average_surfers
    return result

print(solution())