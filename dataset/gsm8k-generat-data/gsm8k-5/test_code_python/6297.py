def solution():
    starting_weight = 250  # Jordan starts with a weight of 250 pounds
    first_4_weeks_loss = 3 * 4  # Jordan loses 3 pounds per week for the first 4 weeks
    remaining_weeks_loss = 2 * 8  # Jordan loses 2 pounds per week for the next 8 weeks

    # Calculate Jordan's weight after the first 12 weeks
    weight_after_12_weeks = starting_weight - first_4_weeks_loss - remaining_weeks_loss

    result = weight_after_12_weeks
    return result

print(solution())