def solution():
    """The tallest building in the world is 100 feet tall. If the second tallest is half that tall, and the third tallest is half as tall as the second, and the fourth is one-fifth as tall as the third, how tall are all 4 buildings put together?"""
    tallest_building = 100
    second_building = tallest_building / 2
    third_building = second_building / 2
    fourth_building = third_building / 5
    total_height = tallest_building + second_building + third_building + fourth_building
    result = total_height
    return result

print(solution())