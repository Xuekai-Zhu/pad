def solution():
    # Find the total number of correct answers of Ella
    correct_answers = 40 - 4  # Ella got 4 incorrect answers

    # Find the score of Marion
    marion_score = (correct_answers / 2) + 6  # Marion got 6 more than half the score of Ella

    result = marion_score
    return result

print(solution())