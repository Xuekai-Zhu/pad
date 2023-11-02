def solution():
    # Calculate the number of questions Mark completed on the first test
    first_test_questions = 75 * 5

    # Calculate the number of questions Mark completed on the second test
    second_test_questions = 100 * 5

    # Calculate the total number of questions Mark completed
    total_questions = first_test_questions + second_test_questions

    # Calculate the number of questions Mark leave incomplete
    incomplete_questions = total_questions - 75
    result = incomplete_questions
    return result

print(solution())