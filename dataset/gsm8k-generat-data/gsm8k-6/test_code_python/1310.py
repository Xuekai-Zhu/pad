def solution():
    # Find the number of true/false problems
    free_response = x  # let x be the number of free response problems
    multiple_choice = 2*x  # twice as many multiple choice problems as free response
    true_false = free_response - 7  # 7 more free response than true/false

    # Calculate the total number of problems
    total_problems = free_response + multiple_choice + true_false  # total number of problems is the sum of all types of problems

    # Check if the total problems assigned match the given number of problems
    if total_problems == 45:
        result = true_false
    else:
        result = "Error: Total number of problems assigned does not match given number of problems"
    return result

print(solution())