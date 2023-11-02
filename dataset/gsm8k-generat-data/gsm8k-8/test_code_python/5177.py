def solution():
    # Calculate the number of incorrect answers Sylvia had
    sylvia_incorrect = 50 / 5

    # Calculate the number of correct answers Sylvia had
    sylvia_correct = 50 - sylvia_incorrect

    # Calculate the number of correct answers Sergio had
    sergio_correct = 50 - 4

    # Calculate the difference in correct answers between Sergio and Sylvia
    difference = sergio_correct - sylvia_correct
    result = difference
    return result

print(solution())