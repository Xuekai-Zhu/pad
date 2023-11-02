def solution():
    """A garden produced 237 potatoes, 60 fewer cucumbers and twice as many peppers than the cucumbers. How many vegetables did the garden produce?"""
    potato_count = 237
    cucumber_count = 60
    pepper_count = cucumber_count * 2
    total_vegetables = potato_count + cucumber_count + pepper_count
    result = total_vegetables
    return result

print(solution())