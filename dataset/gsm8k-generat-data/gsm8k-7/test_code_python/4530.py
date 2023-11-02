def solution():
    num_items = 40
    ella_incorrect = 4

    # Calculate the number of correct answers Ella got
    ella_correct = num_items - ella_incorrect

    # Calculate Marion's score as half of Ella's score plus 6
    marion_score = (ella_correct / 2) + 6
    result = marion_score
    return result

print(solution())