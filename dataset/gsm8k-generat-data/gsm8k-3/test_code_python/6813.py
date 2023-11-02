def solution():
    """The tallest building in the world is 100 feet tall.  If the second tallest is half that tall, and the third tallest is half as tall as the second, and the fourth is one-fifth as tall as the third, how tall are all 4 buildings put together?"""
    # Define the heights of the buildings
    building1 = 100
    building2 = building1 * 0.5
    building3 = building2 * 0.5
    building4 = building3 * 0.2

    # Calculate the total height of all 4 buildings
    total_height = building1 + building2 + building3 + building4

    # Display the total height
    result = total_height
    return result

print(solution())