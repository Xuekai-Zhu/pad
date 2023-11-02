def solution():
    """Stacy is a high school Calculus teacher. She assigns 45 problems for homework. There are twice as many multiple choice problems as free response, and 7 more free response than true/false. How many true/false questions are there?"""
    total_problems = 45
    free_response = x
    true_false = free_response - 7
    multiple_choice = 2 * free_response
    total_problems = free_response + true_false + multiple_choice
    true_false = (total_problems - multiple_choice - 7) / 2
    result = true_false
    return result

print(solution())