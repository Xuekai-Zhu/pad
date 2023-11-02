def solution():
    # Find the total number of parts in the ratio (4+5 = 9 parts)
    total_parts = 4 + 5

    # Find the number of parts Manny has: 5 parts out of 9
    manny_parts = 5 / total_parts

    # Find the number of marbles Manny originally had by multiplying his parts by the total number of marbles
    original_manny_marbles = manny_parts * 36

    # Manny gives 2 marbles to his brother, so he now has 2 less marbles
    remaining_marbles = original_manny_marbles - 2

    result = remaining_marbles
    return result

print(solution())