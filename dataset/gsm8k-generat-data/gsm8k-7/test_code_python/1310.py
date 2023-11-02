def solution():
    total_problems = 45
    num_true_false = 0
    num_free_response = 0
    num_multiple_choice = 0

    # Calculate the number of free response questions
    num_free_response = num_true_false + 7

    # Calculate the number of multiple choice questions
    num_multiple_choice = 2 * num_free_response

    # Calculate the total number of problems
    total_problems = num_true_false + num_free_response + num_multiple_choice

    # Solve for the number of true/false questions
    num_true_false = total_problems - num_free_response - num_multiple_choice

    result = num_true_false
    return result

print(solution())