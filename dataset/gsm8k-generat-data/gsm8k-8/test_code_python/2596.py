def solution():
    # Calculate the average of the first 3 scores
    first_three_avg = (50 + 70 + 66) / 3

    # Calculate the History score
    history_score = first_three_avg

    # Calculate the total score across all 4 subjects
    total_score = 50 + 70 + 66 + history_score

    result = total_score
    return result

print(solution())