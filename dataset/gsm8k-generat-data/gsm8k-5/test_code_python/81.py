def solution():
    sam_round1 = 16
    jeff_round1 = sam_round1 - 1
    jeff_round2 = sam_round1 - 3
    jeff_round3 = sam_round1 + 4
    jeff_round4 = sam_round1 * 2

    # Calculate total skips by Jeff
    total_skips_by_jeff = jeff_round1 + jeff_round2 + jeff_round3 + jeff_round4

    # Calculate average skips by Jeff
    average_skips_by_jeff = total_skips_by_jeff / 4
    result = average_skips_by_jeff
    return result

print(solution())