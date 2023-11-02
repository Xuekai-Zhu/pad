def solution():
    """A tiger shark has 180 teeth. A hammerhead shark has 1/6 the number of teeth that a tiger shark has. A great white shark has double the sum of teeth of a tiger shark and a hammerhead shark. How many teeth does a great white shark have?"""
    # Define the number of teeth of a tiger shark
    tiger_shark_teeth = 180

    # Calculate the number of teeth of a hammerhead shark
    hammerhead_shark_teeth = tiger_shark_teeth * (1/6)

    # Calculate the sum of teeth of a tiger and hammerhead shark
    total_teeth = tiger_shark_teeth + hammerhead_shark_teeth

    # Calculate the number of teeth of a great white shark
    great_white_shark_teeth = total_teeth * 2

    # return the result
    result = great_white_shark_teeth
    return result

print(solution())