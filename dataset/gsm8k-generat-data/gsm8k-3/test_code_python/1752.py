def solution():
    """In a 50-question test with two marks for each question, Meghan learned that she scored 20 marks less than her friend Jose, who scored 40 more marks than their friend Alisson. Calculate the total score for the three in the test combined if Jose got 5 questions wrong?"""
    # Define the number of questions and marks per question
    NUM_QUESTIONS = 50
    MARKS_PER_QUESTION = 2

    # Calculate the total marks possible on the test
    total_marks = NUM_QUESTIONS * MARKS_PER_QUESTION

    # Calculate the number of marks Jose got correct
    jose_correct = (NUM_QUESTIONS - 5) * MARKS_PER_QUESTION

    # Calculate the number of marks Alisson got
    alisson_marks = jose_correct - 40

    # Calculate the number of marks Meghan got
    meghan_marks = jose_correct - 20

    # Calculate the total marks for all three
    total_score = jose_correct + alisson_marks + meghan_marks

    # Display the total score
    result = total_score
    return result

print(solution())