def solution():
    white_to_brown_eggs_ratio = 3  # Linda had three times as many white eggs as brown eggs
    brown_eggs_survived = 5  # All 5 of the brown eggs survived
    total_eggs_left = 12  # Linda had a dozen eggs left after the accident

    # Calculate the number of brown eggs Linda had before the accident
    brown_eggs_before = brown_eggs_survived

    # Calculate the number of white eggs Linda had before the accident
    white_eggs_before = brown_eggs_before * white_to_brown_eggs_ratio

    # Calculate the total number of eggs Linda had before the accident
    total_eggs_before = brown_eggs_before + white_eggs_before

    # Calculate the number of eggs Linda broke
    broken_eggs = total_eggs_before - total_eggs_left
    result = broken_eggs
    return result

print(solution())