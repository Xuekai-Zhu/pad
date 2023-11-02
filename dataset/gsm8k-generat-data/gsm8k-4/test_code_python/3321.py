def solution():
    """John took a test with 80 questions. For the first 40 questions, she got 90% right. For the next 40 questions, she gets 95% right. How many total questions does she get right?"""
    # Define the number of questions and the percentage of correct answers for each section
    total_questions = 80
    section1_percent = 90
    section2_percent = 95

    # Calculate the number of questions John got right in each section
    section1_right = int(total_questions / 2 * (section1_percent / 100))
    section2_right = int(total_questions / 2 * (section2_percent / 100))

    # Calculate the total number of questions John got right
    total_right = section1_right + section2_right

    # return the result
    result = total_right
    return result

print(solution())