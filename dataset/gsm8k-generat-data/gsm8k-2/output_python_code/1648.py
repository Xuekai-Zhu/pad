def solution():
    """In a field of 500 clovers, 20% have four leaves and one quarter of these are purple clovers. Assuming these proportions are exactly correct, how many clovers in the field are both purple and four-leaved?"""
    total_clovers = 500
    four_leaved = 0.2 * total_clovers
    purple_four_leaved = 0.25 * four_leaved
    result = purple_four_leaved
    return result

print(solution())