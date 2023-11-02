def solution():
    """Tom's ship can travel at 10 miles per hour. He is sailing from 1 to 4 PM. He then travels back at a rate of 6 mph. How long does it take him to get back?"""
    distance = 10 * 3  # Distance traveled from 1 to 4 PM
    time_to_return = distance / 6  # Time taken to return at 6 mph
    result = time_to_return
    return result

print(solution())