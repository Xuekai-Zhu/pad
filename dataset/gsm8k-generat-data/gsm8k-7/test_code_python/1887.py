def solution():
    first_answer = 600
    second_answer = first_answer * 2
    third_answer = first_answer + second_answer - 400

    # Calculate the total of August's answers
    total_answers = first_answer + second_answer + third_answer
    result = total_answers
    return result

print(solution())