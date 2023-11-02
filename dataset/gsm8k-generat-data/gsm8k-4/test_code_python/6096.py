def solution():
    """John's grill messes up and burns half his steak. He eats 80% of what isn't burned. If the steak was originally 30 ounces how much steak did he eat?"""
    # Define the original weight of the steak
    original_weight = 30  # in ounces

    # Calculate the weight of the burned portion
    burned_weight = original_weight / 2

    # Calculate the weight of the remaining (unburned) portion
    remaining_weight = original_weight - burned_weight

    # Calculate the weight of the portion that John eats
    eaten_weight = remaining_weight * 0.8

    # Return the result
    result = eaten_weight
    return result

print(solution())