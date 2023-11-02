def solution():
    # Define variables
    current_average = 70
    total_tests = 8
    min_average = 75
    bonus = 500
    additional_bonus = 10
    desired_bonus = 600

    # Calculate the current total score
    current_total_score = current_average * total_tests

    # Calculate the current bonus
    current_bonus = 0
    if current_average > min_average:
        current_bonus = bonus + (current_average - min_average) * additional_bonus

    # Calculate the required total score
    required_total_score = (desired_bonus - bonus) / additional_bonus + total_tests * min_average

    # Calculate the combined score the last two tests need
    last_two_tests = required_total_score - current_total_score

    # Check if the combined score is possible
    if last_two_tests > (150 * 2) or last_two_tests < 0:
        return "Impossible"
    else:
        return last_two_tests

print(solution())