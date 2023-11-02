def solution():
    """Sam and Jeff had a skipping competition at recess. The competition was split into four rounds. Sam completed 1 more skip than Jeff in the first round. Jeff skipped 3 fewer times than Sam in the second round. Jeff skipped 4 more times than Sam in the third round. Jeff got tired and only completed half the number of skips as Sam in the last round. If Sam skipped 16 times in each round, what is the average number of skips per round completed by Jeff?"""
    # Define the number of skips Sam completed in each round
    sam_round1 = 16
    sam_round2 = 16
    sam_round3 = 16
    sam_round4 = 16

    # Define the number of skips Jeff completed in each round
    jeff_round1 = sam_round1 - 1
    jeff_round2 = sam_round2 - 3
    jeff_round3 = sam_round3 + 4
    jeff_round4 = sam_round4 / 2

    # Calculate the total number of skips Jeff completed
    total_skips_jeff = jeff_round1 + jeff_round2 + jeff_round3 + jeff_round4

    # Calculate the average number of skips per round completed by Jeff
    avg_skips_jeff = total_skips_jeff / 4

    result = avg_skips_jeff
    return result

print(solution())