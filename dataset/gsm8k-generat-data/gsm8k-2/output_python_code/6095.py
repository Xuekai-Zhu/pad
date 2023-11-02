def solution():
    """John's grill messes up and burns half his steak. He eats 80% of what isn't burned. If the steak was originally 30 ounces how much steak did he eat?"""
    original_steak = 30
    burned_steak = original_steak / 2
    edible_steak = original_steak - burned_steak
    eaten_steak = 0.8 * edible_steak
    result = eaten_steak
    return result

print(solution())