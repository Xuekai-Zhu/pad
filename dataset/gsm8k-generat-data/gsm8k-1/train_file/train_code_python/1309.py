def solution():
    """Stacy is a high school Calculus teacher. She assigns 45 problems for homework. There are twice as many multiple choice problems as free response, and 7 more free response than true/false. How many true/false questions are there?"""
    total_problems = 45
    free_response = (total_problems - 7) / 3
    multiple_choice = 2 * free_response
    true_false = total_problems - free_response - multiple_choice
    result = true_false
    return result

print(solution())