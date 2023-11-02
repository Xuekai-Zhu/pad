def solution():
    """Sam and Jeff had a skipping competition at recess. The competition was split into four rounds. Sam completed 1 more skip than Jeff in the first round. Jeff skipped 3 fewer times than Sam in the second round. Jeff skipped 4 more times than Sam in the third round. Jeff got tired and only completed half the number of skips as Sam in the last round. If Sam skipped 16 times in each round, what is the average number of skips per round completed by Jeff?"""
    # Define the number of skips Sam completed in each round
    sam_skips = 16

    # Calculate the number of skips Jeff completed in each round
    jeff_round1 = sam_skips - 1
    jeff_round2 = sam_skips - 3
    jeff_round3 = sam_skips + 4
    jeff_round4 = sam_skips / 2

    # Calculate the total number of skips Jeff completed
    total_skips = jeff_round1 + jeff_round2 + jeff_round3 + jeff_round4

    # Calculate the average number of skips completed by Jeff
    average_skips = total_skips / 4

    result = average_skips
    return result

print(solution())