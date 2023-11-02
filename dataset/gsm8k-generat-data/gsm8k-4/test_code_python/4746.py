def solution():
    """Gabriel is looking at her marble sets. She sees that in the first set 10% of her marbles are broken. In the second set, 20% of the marbles are broken. The first set contains 50 marbles. The second set contains 60. How many marbles are broken in total?"""
    # Calculate the number of broken marbles in the first set
    set1_broken = 0.1 * 50

    # Calculate the number of broken marbles in the second set
    set2_broken = 0.2 * 60

    # Calculate the total number of broken marbles
    total_broken = set1_broken + set2_broken

    # return the result
    result = total_broken
    return result

print(solution())