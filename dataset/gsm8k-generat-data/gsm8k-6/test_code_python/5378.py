def solution():
    # Calculate the height of the first 10 stories
    height_first_10 = 10 * 12  # each of the first 10 stories is 12 feet tall

    # Calculate the height of the remaining 10 stories
    height_remaining = 10 * (12 + 3)  # each of the remaining 10 stories is 3 feet taller than the previous one

    # Calculate the total height of the building
    total_height = height_first_10 + height_remaining

    result = total_height
    return result

print(solution())