def solution():
    # Define John's starting weight
    starting_weight = 135

    # Add the weight he gained through training
    training_gain = 265
    total_weight = starting_weight + training_gain

    # Calculate the weight increase from the bracer
    bracer_bonus = total_weight * 6

    # Calculate John's total weight lifting ability
    total_lift = total_weight + bracer_bonus
    result = total_lift
    return result

print(solution())