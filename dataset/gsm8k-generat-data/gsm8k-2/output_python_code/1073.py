def solution():
    """A bathroom has 10 6 inch tiles along its width and 20 6 inch tiles along its length. What is the square footage of the bathroom?"""
    width = 10 * 6 / 12 # Convert to feet
    length = 20 * 6 / 12 # Convert to feet
    area = width * length
    result = area
    return result

print(solution())