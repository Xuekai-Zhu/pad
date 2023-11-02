def solution():
    """James builds a 20 story building. The first 10 stories are each 12 feet tall each. The remaining floors are each 3 feet taller. How tall is the building?"""
    # Define the height of the first 10 stories
    height_first_10 = 10 * 12

    # Define the height of the remaining stories (11-20)
    height_remaining = (20-10) * (12+3)

    # Calculate the total height of the building
    total_height = height_first_10 + height_remaining

    # return the result
    result = total_height
    return result

print(solution())