def solution():
    # Calculate total marks for the test
    total_marks = 50 * 2

    # Calculate Jose's correct answers
    jose_correct = 50 - 5

    # Calculate Jose's total score
    jose_score = jose_correct * 2

    # Calculate Meghan's score
    meghan_score = jose_score - 20

    # Calculate Alisson's score
    alisson_score = jose_score - 40

    # Calculate total score for all three
    total_score = jose_score + meghan_score + alisson_score
    result = total_score
    return result

print(solution())