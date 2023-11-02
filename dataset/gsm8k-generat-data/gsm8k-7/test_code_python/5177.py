def solution():
    total_questions = 50
    sylvia_incorrect = total_questions / 5
    sergio_incorrect = 4
    sylvia_correct = total_questions - sylvia_incorrect
    sergio_correct = total_questions - sergio_incorrect
    difference = sergio_correct - sylvia_correct
    result = difference
    return result

print(solution())