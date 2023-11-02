def solution():
    # Calculate the time it takes for each popsicle to melt
    time_popsicle_1 = 1
    time_popsicle_2 = 2 * time_popsicle_1
    time_popsicle_3 = 2 * time_popsicle_2
    time_popsicle_4 = 2 * time_popsicle_3
    time_popsicle_5 = 2 * time_popsicle_4
    time_popsicle_6 = 2 * time_popsicle_5

    # Calculate the rate of melting for the last popsicle compared to the first
    rate_of_melting = time_popsicle_1 / time_popsicle_6
    result = rate_of_melting
    return result

print(solution())