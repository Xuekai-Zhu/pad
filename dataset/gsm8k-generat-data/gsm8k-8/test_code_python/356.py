def solution():
    # Define the points for correct answers and bonus
    correct_answer_points = 2
    bonus_points = 4

    # Calculate the total number of questions
    total_questions = 5 * 5

    # Calculate the number of correct answers
    correct_answers = total_questions - 1

    # Calculate the points for correct answers and bonus
    points_for_correct_answers = correct_answers * correct_answer_points
    bonus = bonus_points if correct_answers == total_questions else 0

    # Calculate the total points
    total_points = points_for_correct_answers + bonus
    result = total_points
    return result

print(solution())