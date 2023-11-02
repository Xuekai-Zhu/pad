def solution():
    starting_weight = 250
    first_4_weeks_loss = 3 * 4
    remaining_weeks_loss = 2 * 8

    # Calculate Jordan's weight after the first 4 weeks
    after_first_4_weeks = starting_weight - first_4_weeks_loss

    # Calculate Jordan's weight after the remaining 8 weeks
    after_remaining_weeks = after_first_4_weeks - remaining_weeks_loss

    result = after_remaining_weeks
    return result

print(solution())