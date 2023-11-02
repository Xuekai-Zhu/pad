def solution():
    # Calculate the total points Amanda needs to earn for an A
    total_points_needed = 5 * 93  # an A requires an average of 93% over the 5 quizzes

    # Calculate the total points Amanda has earned so far
    total_points_earned = 4 * 92  # Amanda has averaged 92% on the previous 4 quizzes

    # Calculate the minimum score Amanda needs on the final quiz
    score_needed = (total_points_needed - total_points_earned) / 1  # the final quiz is worth the same as each previous quiz
    result = score_needed
    return result

print(solution())