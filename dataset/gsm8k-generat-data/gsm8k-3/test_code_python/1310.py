def solution():
    """Stacy is a high school Calculus teacher.  She assigns 45 problems for homework.  There are twice as many multiple choice problems as free response, and 7 more free response than true/false.  How many true/false questions are there?"""
    # Define the number of free response questions and true/false questions
    free_response = x
    true_false = x - 7

    # Calculate the number of multiple choice questions
    multiple_choice = 2 * free_response

    # Calculate the total number of questions
    total_questions = free_response + true_false + multiple_choice

    # Check that the total number of questions is equal to 45
    assert total_questions == 45, "Total number of questions is not equal to 45!"

    # Solve for the number of true/false questions
    true_false = (45 - 3 * free_response) / 2

    # Display the number of true/false questions
    result = true_false
    return result

print(solution())