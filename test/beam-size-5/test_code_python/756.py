def solution():
    # Calculate the number of people who think horse #2 will win the big race
    num_horse_2 = 0.2 * 50

    # Calculate the number of people who did not win the big race
    num_remaining = 50 - num_horse_2

    # Calculate the number of people who think horse #7 will win the big race
    num_horse_7 = 0.6 * num_remaining

    # Calculate the number of people who think horse #12 will win the big race
    num_horse_12 = num_remaining - num_horse_7

    result = num_horse_12
    return result

print(solution())