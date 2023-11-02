def solution():
    first_answer = 600  # The first math problem's answer is 600
    second_answer = first_answer * 2  # The second math problem's answer is twice as big as the first answer
    third_answer = (first_answer + second_answer) - 400  # The third math problem's answer is 400 less than the combined total of the first two answers

    # Calculate the total of August's answers
    total = first_answer + second_answer + third_answer
    result = total
    return result

print(solution())