def solution():
    height_first_10_stories = 10 * 12  # The first 10 stories are each 12 feet tall
    height_remaining_stories = 10 * (12 + 3)  # The remaining stories are each 3 feet taller than the previous one
    total_height = height_first_10_stories + height_remaining_stories
    result = total_height
    return result

print(solution())