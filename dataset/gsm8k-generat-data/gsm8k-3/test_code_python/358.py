def solution():
    """Students at Highridge High earn 2 points for each correct answer during a quiz bowl If a student correctly answers all the questions in a round, the student is awarded an additional 4 point bonus. They played a total of five rounds each consisting of five questions. If James only missed one question, how many points did he get?"""
    # Define the points for a correct answer and the bonus for answering all questions in a round
    CORRECT_POINTS = 2
    ROUND_BONUS = 4

    # Define the number of rounds and questions per round
    NUM_ROUNDS = 5
    QUESTIONS_PER_ROUND = 5

    # Calculate the total number of questions and James' number of correct answers
    total_questions = NUM_ROUNDS * QUESTIONS_PER_ROUND
    correct_answers = total_questions - 1

    # Calculate James' score
    score = correct_answers * CORRECT_POINTS
    if correct_answers == total_questions:
        score += ROUND_BONUS * NUM_ROUNDS

    # Display James' score
    result = score
    return result

print(solution())