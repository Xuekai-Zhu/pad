def solution():
    current_total_score = 8 * 70  # The current total score from the 8 tests Karen has graded
    current_average_score = current_total_score / 8  # The current average score
    remaining_bonus = 600 - 500  # The additional $100 Karen wants to earn
    additional_points_needed = remaining_bonus / 10  # The number of additional points needed to earn the remaining bonus
    total_points_needed = (8 + 2) * 75 + additional_points_needed * 2  # The total number of points needed to earn the bonus, including the last two tests
    combined_score_needed = total_points_needed - current_total_score  # The combined score needed for the last two tests

    result = combined_score_needed
    return result

print(solution())