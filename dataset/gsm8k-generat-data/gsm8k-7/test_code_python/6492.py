def solution():
    num_crows_1 = 3
    num_worms_1 = 30
    num_crows_2 = 5
    num_hours_2 = 2

    # Calculate the rate of consumption for 3 crows
    rate_1 = num_worms_1 / num_crows_1

    # Calculate the total number of worms consumed by 5 crows in 2 hours
    num_worms_2 = rate_1 * num_crows_2 * num_hours_2
    result = num_worms_2
    return result

print(solution())