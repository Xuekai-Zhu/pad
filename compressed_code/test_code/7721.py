def solution():
    
    bobs_skips_per_rock = 12
    jims_skips_per_rock = 15
    rocks_skipped = 10
    total_skips = (bobs_skips_per_rock + jims_skips_per_rock) * rocks_skipped
    result = total_skips
    return result

print(solution())