def solution():
    """Stacy is a high school Calculus teacher. She assigns 45 problems for homework. There are twice as many multiple choice problems as free response, and 7 more free response than true/false. How many true/false questions are there?"""
    # Define the total number of problems
    total_problems = 45

    # Calculate the number of true/false questions
    tf_questions = (total_problems - 7) / 4

    # return the result
    result = tf_questions
    return result

print(solution())