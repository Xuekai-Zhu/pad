def solution():
    """Bob and Jim decide to skip rocks. Bob can skip a rock 12 times. Jim can skip a rock 15 times. If they each skipped 10 rocks how many total skips did they get?"""
    bobs_skips_per_rock = 12
    jims_skips_per_rock = 15
    rocks_skipped = 10
    total_skips = (bobs_skips_per_rock + jims_skips_per_rock) * rocks_skipped
    result = total_skips
    return result

print(solution())