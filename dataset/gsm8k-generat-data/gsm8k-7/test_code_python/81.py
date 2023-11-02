def solution():
    sam_round1 = 16
    jeff_round1 = sam_round1 - 1
    jeff_round2 = sam_round1 - 3
    jeff_round3 = sam_round1 + 4
    jeff_round4 = sam_round1 * 0.5

    total_skips = sam_round1 * 4 + jeff_round1 + jeff_round2 + jeff_round3 + jeff_round4
    num_rounds = 4

    # Calculate the average number of skips per round completed by Jeff
    jeff_average = (total_skips - sam_round1 * 4) / (num_rounds - 1)

    result = jeff_average
    return result

print(solution())