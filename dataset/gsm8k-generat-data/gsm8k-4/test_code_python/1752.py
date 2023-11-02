def solution():
    """In a 50-question test with two marks for each question, Meghan learned that she scored 20 marks less than her friend Jose, who scored 40 more marks than their friend Alisson. Calculate the total score for the three in the test combined if Jose got 5 questions wrong?"""
    # Define the total number of questions and marks per question
    total_questions = 50
    marks_per_question = 2

    # Calculate the total marks available in the test
    total_marks = total_questions * marks_per_question

    # Calculate the number of questions Jose got right
    jose_questions_right = total_questions - 5
    jose_marks = jose_questions_right * marks_per_question

    # Calculate Alisson's marks
    alisson_marks = jose_marks - 40

    # Calculate Meghan's marks
    meghan_marks = jose_marks - 20

    # Calculate the total score for all three
    total_score = jose_marks + alisson_marks + meghan_marks

    result = total_score
    return result

print(solution())