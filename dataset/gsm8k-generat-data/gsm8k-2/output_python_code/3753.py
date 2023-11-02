def solution():
    """A tiger shark has 180 teeth. A hammerhead shark has 1/6 the number of teeth that a tiger shark has. A great white shark has double the sum of teeth of a tiger shark and a hammerhead shark. How many teeth does a great white shark have?"""
    tiger_shark_teeth = 180
    hammerhead_shark_teeth = tiger_shark_teeth / 6
    great_white_shark_teeth = 2 * (tiger_shark_teeth + hammerhead_shark_teeth)
    result = great_white_shark_teeth
    return result

print(solution())