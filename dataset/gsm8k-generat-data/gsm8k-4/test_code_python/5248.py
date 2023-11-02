def solution():
    """John used to be able to squat 135 pounds. After training, he increased that by 265 pounds. He then gets a magical strength-increasing bracer that increases his strength by an additional 600%. How much can he now lift?"""
    # Define John's starting squat weight and the weight increase from his training
    starting_weight = 135
    training_increase = 265

    # Calculate John's weight after training
    weight_after_training = starting_weight + training_increase

    # Calculate John's weight after using the magical bracer
    weight_with_bracer = weight_after_training * 7

    # Return the result
    result = weight_with_bracer
    return result

print(solution())