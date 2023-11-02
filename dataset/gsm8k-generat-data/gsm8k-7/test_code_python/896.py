def solution():
    easy_points = 2
    average_points = 3
    hard_points = 5

    num_easy_correct = 6
    num_average_correct = 2
    num_hard_correct = 4

    # Calculate the total points for all correct answers in each round
    easy_total = easy_points * num_easy_correct
    average_total = average_points * num_average_correct
    hard_total = hard_points * num_hard_correct

    # Calculate the overall total points
    total_points = easy_total + average_total + hard_total
    result = total_points
    return result

print(solution())