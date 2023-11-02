def solution():
    # We can use the formula for the average of n numbers: (sum of numbers) / n
    # We know Lizette's overall average, and we have one quiz score, so we can solve for the sum of the first two quiz scores
    overall_average = 94
    third_quiz_score = 92
    sum_of_first_two_quizzes = overall_average * 3 - third_quiz_score
    # We divide this sum by 2 to get the average of the first two quizzes
    average_of_first_two_quizzes = sum_of_first_two_quizzes / 2
    result = average_of_first_two_quizzes
    return result

print(solution())