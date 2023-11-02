def solution():
    """Gabriel is looking at her marble sets. She sees that in the first set 10% of her marbles are broken. In the second set, 20% of the marbles are broken. The first set contains 50 marbles. The second set contains 60. How many marbles are broken in total?"""
    first_set_size = 50
    first_set_broken_perc = 0.1
    second_set_size = 60
    second_set_broken_perc = 0.2
    total_broken = first_set_size * first_set_broken_perc + second_set_size * second_set_broken_perc
    result = total_broken
    return result

print(solution())