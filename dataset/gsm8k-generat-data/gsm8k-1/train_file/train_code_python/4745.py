def solution():
    """Gabriel is looking at her marble sets. She sees that in the first set 10% of her marbles are broken. In the second set, 20% of the marbles are broken. The first set contains 50 marbles. The second set contains 60. How many marbles are broken in total?"""
    set1_size = 50
    set2_size = 60
    set1_broken = set1_size * 0.1
    set2_broken = set2_size * 0.2
    total_broken = set1_broken + set2_broken
    result = total_broken
    return result

print(solution())