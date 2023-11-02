def solution():
    # Calculate the number of incorrect answers for Sylvia
    incorrect_sylvia = 50 * (1/5)

    # Calculate the number of incorrect answers for Sergio
    incorrect_sergio = 4

    # Calculate the number of correct answers for Sylvia
    correct_sylvia = 50 - incorrect_sylvia

    # Calculate the number of correct answers for Sergio
    correct_sergio = 50 - incorrect_sergio

    # Calculate the difference between Sergio and Sylvia's correct answers
    difference = correct_sergio - correct_sylvia
    result = difference
    return result

print(solution())