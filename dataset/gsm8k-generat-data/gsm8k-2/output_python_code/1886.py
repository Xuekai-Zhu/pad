def solution():
    """On his calculator, August had solved a math problem with an answer of 600. The following math problem had an answer twice as big as the answer of the first math problem, and the third math problem had an answer 400 less than the combined total answers of the first and the second math problems. What's the total of August's answers from solving the three math problems on his calculator?"""
    first_answer = 600
    second_answer = 2 * first_answer
    third_answer = first_answer + second_answer - 400
    total_answers = first_answer + second_answer + third_answer
    result = total_answers
    return result

print(solution())