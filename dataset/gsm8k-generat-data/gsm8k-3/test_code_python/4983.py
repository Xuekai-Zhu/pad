def solution():
    """Violet is planning a hike through the desert with her dog. Violet needs 800 ml of water per hour hiked and her dog needs 400 ml of water per hour. If Violet can carry 4.8 L of water, how many hours can she and her dog spend hiking?"""
    # Define the water needs for Violet and her dog per hour
    VIOLET_NEEDS = 800
    DOG_NEEDS = 400

    # Define the total amount of water Violet can carry
    TOTAL_WATER = 4.8  # L

    # Calculate the maximum number of hours they can hike
    max_hours = TOTAL_WATER / ((VIOLET_NEEDS + DOG_NEEDS) / 1000)

    # Display the maximum number of hours
    result = max_hours
    return result

print(solution())