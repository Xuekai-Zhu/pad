def solution():
    """On his calculator, August had solved a math problem with an answer of 600. The following math problem had an answer twice as big as the answer of the first math problem, and the third math problem had an answer 400 less than the combined total answers of the first and the second math problems. What's the total of August's answers from solving the three math problems on his calculator?"""
    answer1 = 600
    answer2 = 2 * answer1
    answer3 = (answer1 + answer2) - 400
    total = answer1 + answer2 + answer3
    result = total
    return result

print(solution())