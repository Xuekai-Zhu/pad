def solution():
    # Calculate Larry's shoulder height
    larry_height = 5  # Larry's height is 5 feet
    larry_shoulder_height = 0.8 * larry_height  # Larry's shoulder height is 20% less than his full height

    # Calculate the total height they can reach while Barry stands on Larry's shoulders
    total_height_reached = larry_shoulder_height + 5  # Barry can reach apples that are 5 feet high
    result = total_height_reached
    return result

print(solution())