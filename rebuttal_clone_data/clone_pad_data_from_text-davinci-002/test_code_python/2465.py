def solution():
    twigs_needed = 12
    twigs_per_addition = 6
    twigs_available = twigs_needed * (1/3)
    twigs_missing = twigs_needed - twigs_available
    twigs_to_find = twigs_missing * twigs_per_addition
    result = twigs_to_find
    return result

print(solution())