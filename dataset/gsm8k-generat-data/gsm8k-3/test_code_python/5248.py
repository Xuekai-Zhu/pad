def solution():
    """John used to be able to squat 135 pounds.  After training, he increased that by 265 pounds.  He then gets a magical strength-increasing bracer that increases his strength by an additional 600%.  How much can he now lift?"""
    # Define John's starting weight
    starting_weight = 135

    # Add the weight he gained from training
    training_weight = 265
    total_weight = starting_weight + training_weight

    # Calculate the weight increase from the bracer
    bracer_multiplier = 6
    bracer_increase = total_weight * bracer_multiplier

    # Calculate John's new total weight
    new_weight = total_weight + bracer_increase

    # Display John's new weight
    result = new_weight
    return result

print(solution())