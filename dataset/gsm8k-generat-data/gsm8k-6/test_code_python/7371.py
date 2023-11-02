def solution():
    # Calculate the current total score of the first 8 tests
    current_total_score = 8 * 70

    # Calculate the combined score needed for the last two tests to earn a $600 bonus
    combined_score_needed = (75 * 10 + 500 + 600 - current_total_score) / 2

    result = combined_score_needed
    return result

print(solution())