def solution():
    total_num_questions = 80
    first_40_correct = int(0.9 * 40)
    next_40_correct = int(0.95 * 40)

    # Calculate the total number of questions John got right
    total_correct = first_40_correct + next_40_correct
    result = total_correct
    return result

print(solution())