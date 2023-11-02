def solution():
    original_steak = 30  # The steak was originally 30 ounces
    burned_steak = original_steak / 2  # Half of the steak was burned
    edible_steak = original_steak - burned_steak  # The remaining edible steak

    # John eats 80% of the edible steak
    eaten_steak = 0.8 * edible_steak
    result = eaten_steak
    return result

print(solution())