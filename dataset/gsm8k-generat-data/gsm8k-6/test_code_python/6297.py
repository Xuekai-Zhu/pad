def solution():
    starting_weight = 250  # starting weight in pounds
    weight_loss_first_4_weeks = 3 * 4  # weight lost in the first 4 weeks, 3 pounds per week
    weight_loss_remaining_8_weeks = 2 * 8  # weight lost in the remaining 8 weeks, 2 pounds per week

    # Calculate the current weight of Jordan
    current_weight = starting_weight - weight_loss_first_4_weeks - weight_loss_remaining_8_weeks

    result = current_weight
    return result

print(solution())