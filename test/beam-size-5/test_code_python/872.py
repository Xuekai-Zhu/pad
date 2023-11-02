def solution():
    num_multiple_choice = 10
    num_multiple_choice_percent = 0.8
    num_true_false_percent = 0.9
    num_long_answer_percent = 0.6

    num_multiple_choice_points = num_multiple_choice * num_multiple_choice_percent
    num_true_false_points = num_true_false_percent * num_multiple_choice_percent
    num_long_answer_points = num_long_answer_percent * num_long_answer_percent

    # Calculate the total points scored by Amy
    total_points_scored = (num_multiple_choice_points * num_multiple_choice_percent) + (num_true_false_points * num_success_points) + (num_long_answer_points * num_long_answer_points)
    result = total_points_scored
    return result

print(solution())