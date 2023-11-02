def solution():
    """On his calculator, August had solved a math problem with an answer of 600. The following math problem had an answer twice as big as the answer of the first math problem, and the third math problem had an answer 400 less than the combined total answers of the first and the second math problems. What's the total of August's answers from solving the three math problems on his calculator?"""
    # Solve the first math problem
    answer1 = 600

    # Solve the second math problem
    answer2 = 2 * answer1

    # Solve the third math problem
    answer3 = answer1 + answer2 - 400

    # Calculate the total of all three answers
    total = answer1 + answer2 + answer3

    # Display the total
    result = total
    return result

print(solution())