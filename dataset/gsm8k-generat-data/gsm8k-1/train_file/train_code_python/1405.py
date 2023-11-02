def solution():
    """Bill is trying to count the toddlers at his daycare, but they keep running around. He double-counts 8 toddlers and misses 3 who are hiding. If Bill thinks he counted 26 toddlers, how many are there really?"""
    counted_toddlers = 26
    double_counted = 8
    missed = 3
    true_count = (counted_toddlers - double_counted) + missed
    result = true_count
    return result

print(solution())