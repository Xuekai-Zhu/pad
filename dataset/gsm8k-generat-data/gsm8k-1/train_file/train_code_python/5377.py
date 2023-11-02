def solution():
    """James builds a 20 story building. The first 10 stories are each 12 feet tall each. The remaining floors are each 3 feet taller. How tall is the building?"""
    first_ten_stories_height = 10 * 12
    remaining_stories_height = 10 * (12 + 3)
    total_height = first_ten_stories_height + remaining_stories_height
    result = total_height
    return result

print(solution())