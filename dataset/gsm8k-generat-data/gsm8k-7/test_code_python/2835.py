def solution():
    day1_surfers = 1500
    day2_surfers = day1_surfers + 600
    day3_surfers = day1_surfers * (2/5)

    # Calculate the total number of surfers for all three days
    total_surfers = day1_surfers + day2_surfers + day3_surfers

    # Calculate the average number of surfers for the three days
    average_surfers = total_surfers / 3

    result = average_surfers
    return result

print(solution())