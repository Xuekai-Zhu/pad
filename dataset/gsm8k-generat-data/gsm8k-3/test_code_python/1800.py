def solution():
    """In a Geometry exam, Madeline got 2 mistakes which are half as many mistakes as Leo. Brent scored 25 and has 1 more mistake than Leo. What is Madeline's score?"""
    # Define Leo's number of mistakes
    leo_mistakes = 2 * 2

    # Define Brent's number of mistakes
    brent_mistakes = leo_mistakes + 1

    # Define the total number of questions in the exam
    total_questions = 25 + leo_mistakes + brent_mistakes

    # Calculate the number of correct answers Madeline got
    madeline_correct = total_questions - (2 + leo_mistakes)

    # Calculate Madeline's score
    madeline_score = madeline_correct / total_questions * 100

    # Display Madeline's score
    result = madeline_score
    return result

print(solution())