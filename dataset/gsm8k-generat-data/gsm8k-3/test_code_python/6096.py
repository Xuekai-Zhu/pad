def solution():
    """John's grill messes up and burns half his steak. He eats 80% of what isn't burned. If the steak was originally 30 ounces how much steak did he eat?"""
    # Calculate the amount of burned steak
    burned_steak = 0.5 * 30  # Half of the original 30 ounces

    # Calculate the amount of edible steak
    edible_steak = 30 - burned_steak  # Subtract the burned steak from the original 30 ounces

    # Calculate the amount of steak John eats
    eaten_steak = 0.8 * edible_steak  # 80% of what is left after the burning
    result = eaten_steak
    return result

print(solution())