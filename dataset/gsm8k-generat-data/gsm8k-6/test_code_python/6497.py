def solution():
    # Find the total number of parts in the ratio
    total_parts = 4 + 5  # 4 parts for Mario and 5 parts for Manny

    # Find the number of parts Manny has
    manny_parts = 5/total_parts * 36

    # Subtract 2 marbles from Manny's share
    manny_marbles = manny_parts - 2
    result = manny_marbles
    return result

print(solution())