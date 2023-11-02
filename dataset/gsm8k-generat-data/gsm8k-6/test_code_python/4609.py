def solution():
    # Calculate the total score Lizette had in her first two quizzes
    total_score = 94 * 3 - 92  # her total score after her third quiz is her average multiplied by three, subtract the score from her third quiz to get the total score of the first two quizzes
    average_first_two_quizzes = total_score / 2  # divide total score by 2 to get the average score of the first two quizzes
    result = average_first_two_quizzes
    return result

print(solution())