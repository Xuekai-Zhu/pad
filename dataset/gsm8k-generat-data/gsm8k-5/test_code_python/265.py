def solution():
    barry_reach = 5  # Barry can reach apples that are 5 feet high
    larry_height = 5  # Larry is 5 feet tall
    larry_shoulder_height = 0.8 * larry_height  # Larry's shoulder height is 20% less than his full height
    combined_reach = barry_reach + larry_shoulder_height  # Barry and Larry's combined reach

    result = combined_reach
    return result

print(solution())