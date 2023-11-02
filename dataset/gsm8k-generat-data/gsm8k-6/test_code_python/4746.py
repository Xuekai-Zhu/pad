def solution():
    # Calculate the number of broken marbles in each set
    broken_set1 = 0.1 * 50  # 10% of 50 marbles are broken
    broken_set2 = 0.2 * 60  # 20% of 60 marbles are broken

    # Calculate the total number of broken marbles
    total_broken = broken_set1 + broken_set2
    result = total_broken
    return result

print(solution())