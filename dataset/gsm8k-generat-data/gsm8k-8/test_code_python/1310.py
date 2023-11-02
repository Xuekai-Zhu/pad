def solution():
    # Define the number of free response problems
    free_response = 2 * (true_false + 7)

    # Calculate the total number of problems
    total_problems = 45

    # Set up an equation using the total number of problems and the number of each type of problem
    # true_false + free_response + 2 * free_response = total_problems
    # Substitute the expression for free_response and solve for true_false
    true_false = (total_problems - 3 * free_response) / 3

    result = true_false
    return result

print(solution())