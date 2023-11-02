def solution():
    num_questions = 50
    marks_per_question = 2
    
    # calculate total marks for the test
    total_marks = num_questions * marks_per_question
    
    # calculate Jose's marks
    jose_marks = total_marks - 10   # Jose got 5 questions wrong, so he lost 10 marks
    
    # calculate Alisson's marks
    alisson_marks = jose_marks - 40
    
    # calculate Meghan's marks
    meghan_marks = jose_marks - 20
    
    # calculate total marks for all three friends
    total_score = jose_marks + alisson_marks + meghan_marks
    result = total_score
    return result

print(solution())