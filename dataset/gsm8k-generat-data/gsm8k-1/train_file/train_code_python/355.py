def solution():
    """Students at Highridge High earn 2 points for each correct answer during a quiz bowl If a student correctly answers all the questions in a round, the student is awarded an additional 4 point bonus. They played a total of five rounds each consisting of five questions. If James only missed one question, how many points did he get?"""
    points_per_question = 2
    bonus_points = 4
    questions_per_round = 5
    rounds_played = 5
    questions_correct = (questions_per_round * rounds_played) - 1
    total_points = (questions_correct * points_per_question) + bonus_points
    result = total_points
    return result

print(solution())