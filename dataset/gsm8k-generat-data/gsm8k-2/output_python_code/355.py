def solution():
    """Students at Highridge High earn 2 points for each correct answer during a quiz bowl. If a student correctly answers all the questions in a round, the student is awarded an additional 4 point bonus. They played a total of five rounds each consisting of five questions. If James only missed one question, how many points did he get?"""
    num_answers = 24 # James answered 24 out of 25 questions correctly
    num_rounds = 5
    num_correct_rounds = 4 # James missed one question in one round
    bonus_points = 4 * num_correct_rounds
    total_points = (num_answers * 2) + bonus_points
    result = total_points
    return result

print(solution())