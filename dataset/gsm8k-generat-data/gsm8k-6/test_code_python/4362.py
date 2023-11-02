def solution():
    # Calculate the number of questions Phillip gets right on the math test
    math_correct = 0.75 * 40

    # Calculate the number of questions Phillip gets right on the English test
    english_correct = 0.98 * 50

    # Calculate the total number of questions Phillip gets right
    total_correct = math_correct + english_correct
    result = total_correct
    return result

print(solution())