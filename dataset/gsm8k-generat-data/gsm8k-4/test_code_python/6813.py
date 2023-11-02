def solution():
    """The tallest building in the world is 100 feet tall. If the second tallest is half that tall, and the third tallest is half as tall as the second, and the fourth is one-fifth as tall as the third, how tall are all 4 buildings put together?"""
    # Define the height of the first building
    building1 = 100

    # Calculate the height of the second building
    building2 = building1 / 2

    # Calculate the height of the third building
    building3 = building2 / 2

    # Calculate the height of the fourth building
    building4 = building3 / 5

    # Calculate the total height of all four buildings
    total_height = building1 + building2 + building3 + building4

    result = total_height
    return result

print(solution())