def solution():
    """In a 50-question test with two marks for each question, Meghan learned that she scored 20 marks less than her friend Jose, who scored 40 more marks than their friend Alisson. Calculate the total score for the three in the test combined if Jose got 5 questions wrong?"""
    total_questions = 50
    marks_per_question = 2
    jose_wrong_questions = 5
    jose_total_marks = (total_questions - jose_wrong_questions) * marks_per_question
    alisson_total_marks = jose_total_marks - 40
    meghan_total_marks = alisson_total_marks - 20
    total_marks = jose_total_marks + alisson_total_marks + meghan_total_marks
    result = total_marks
    return result

print(solution())