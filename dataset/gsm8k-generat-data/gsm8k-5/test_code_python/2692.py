def solution():
    current_total = 90 + 98 + 92 + 94 # Randy's current total score after 4 quizzes
    desired_average = 94 # Randy's desired average score after 5 quizzes
    num_of_quizzes = 5 # Randy is taking a total of 5 quizzes

    # Calculate the minimum score Randy needs to get on his fifth quiz to reach his desired average
    required_score = (desired_average * num_of_quizzes) - current_total
    result = required_score
    return result

print(solution())