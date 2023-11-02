def solution():
    starting_weight = 135
    training_increase = 265
    bracer_increase = 600 # expressed as a percentage
    bracer_multiplier = 1 + (bracer_increase / 100)

    # Calculate John's new maximum lifting weight after training
    new_weight = starting_weight + training_increase

    # Calculate John's new maximum lifting weight after the bracer
    final_weight = new_weight * bracer_multiplier
    result = final_weight
    return result

print(solution())