def solution():
    # Define the number of skips Sam completed in each round
    sam_round1 = 16
    sam_round2 = 16
    sam_round3 = 16
    sam_round4 = 16

    # Calculate the number of skips Jeff completed in each round
    jeff_round1 = sam_round1 - 1
    jeff_round2 = jeff_round1 - 3
    jeff_round3 = jeff_round2 + 4
    jeff_round4 = sam_round4 / 2

    # Calculate the total number of skips completed by Jeff
    total_skips = jeff_round1 + jeff_round2 + jeff_round3 + jeff_round4

    # Calculate the average number of skips per round completed by Jeff
    average_skips_j = total_skips / 4
    result = average_skips_j
    return result

print(solution())