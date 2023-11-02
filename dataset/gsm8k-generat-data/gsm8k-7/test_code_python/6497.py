def solution():
    # Use the ratio 4:5 to determine how many marbles each person should have initially
    total_parts = 4 + 5  # sum of the parts in the ratio
    mario_share = 36 * (4 / total_parts)
    manny_share = 36 * (5 / total_parts)

    # Manny gave 2 marbles to his brother, so update his share
    manny_share -= 2

    result = manny_share
    return result

print(solution())