def solution():
    sams_skips = 16  # Sam skipped 16 times in each round
    jeffs_round1_skips = sams_skips - 1  # Jeff completed 1 fewer skip than Sam in round 1
    jeffs_round2_skips = sams_skips - 3  # Jeff completed 3 fewer skips than Sam in round 2
    jeffs_round3_skips = sams_skips + 4  # Jeff completed 4 more skips than Sam in round 3
    jeffs_round4_skips = sams_skips / 2  # Jeff completed half the number of skips as Sam in round 4
    total_skips = jeffs_round1_skips + jeffs_round2_skips + jeffs_round3_skips + jeffs_round4_skips
    average_skips = total_skips / 4
    result = average_skips
    return result

print(solution())