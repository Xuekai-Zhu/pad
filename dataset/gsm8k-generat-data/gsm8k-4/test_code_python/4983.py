def solution():
    """Violet is planning a hike through the desert with her dog. Violet needs 800 ml of water per hour hiked and her dog needs 400 ml of water per hour. If Violet can carry 4.8 L of water, how many hours can she and her dog spend hiking?"""
    # Define the amount of water Violet and her dog need per hour
    water_per_hour = 800 + 400

    # Define the total amount of water Violet can carry
    total_water = 4.8 * 1000

    # Calculate the number of hours Violet and her dog can spend hiking
    hours = total_water // water_per_hour

    # Return the result
    result = hours
    return result

print(solution())