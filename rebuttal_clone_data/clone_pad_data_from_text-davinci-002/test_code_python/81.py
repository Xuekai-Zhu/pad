def solution():
    """Sam and Jeff had a skipping competition at recess. The competition was split into four rounds. Sam completed 1 more skip than Jeff in the first round. Jeff skipped 3 fewer times than Sam in the second round. Jeff skipped 4 more times than Sam in the third round. Jeff got tired and only completed half the number of skips as Sam in the last round. If Sam skipped 16 times in each round, what is the average number of skips per round completed by Jeff?"""
    skips_per_round = 16
    total_skips = skips_per_round * 4
    skips_completed_by_jeff = total_skips / 2
    result = skips_completed_by_jeff
    return result

print(solution())