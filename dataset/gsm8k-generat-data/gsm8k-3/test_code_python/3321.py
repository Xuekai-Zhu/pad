def solution():
    """John took a test with 80 questions.  For the first 40 questions, she got 90% right.  For the next 40 questions, she gets 95% right.  How many total questions does she get right?"""
    # Define the number of questions and the percentage correct for each set
    QUESTIONS_PER_SET = 40
    SET1_PERCENTAGE = 90
    SET2_PERCENTAGE = 95

    # Calculate the number of questions John gets right in each set
    set1_correct = QUESTIONS_PER_SET * SET1_PERCENTAGE / 100
    set2_correct = QUESTIONS_PER_SET * SET2_PERCENTAGE / 100

    # Calculate the total number of questions John gets right
    total_correct = set1_correct + set2_correct

    # Display the total number of questions John gets right
    result = total_correct
    return result

print(solution())