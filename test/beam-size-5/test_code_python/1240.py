def solution():
    # Calculate the number of questions Audrey needs to correct on the first test
    first_test_correct = 0.7 * 70

    # Calculate the number of questions Audrey needs to get right on the second test
    second_test_correct = 0.6 * 40

    # Calculate the number of questions Audrey needs to get right on the second test
    second_test_correct = 40 - first_test_correct

    result = second_test_correct
    return result

print(solution())