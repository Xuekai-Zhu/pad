def solution():
    """Students at Highridge High earn 2 points for each correct answer during a quiz bowl. If a student correctly answers all the questions in a round, the student is awarded an additional 4 point bonus. They played a total of five rounds each consisting of five questions. If James only missed one question, how many points did he get?"""
    # Define the number of points earned for each correct answer
    CORRECT_ANSWER_POINTS = 2

    # Define the number of rounds and questions per round
    ROUNDS = 5
    QUESTIONS_PER_ROUND = 5

    # Define the number of questions James missed
    questions_missed = 1

    # Calculate the total number of questions James answered correctly
    questions_correct = (ROUNDS * QUESTIONS_PER_ROUND) - questions_missed

    # Calculate the total number of points James earned from correct answers
    correct_answer_points = questions_correct * CORRECT_ANSWER_POINTS

    # Check if James answered all questions correctly and award the bonus points if so
    if questions_missed == 0:
        bonus_points = 4
    else:
        bonus_points = 0

    # Calculate the total number of points James earned
    total_points = correct_answer_points + bonus_points

    # Return the result
    result = total_points
    return result

print(solution())