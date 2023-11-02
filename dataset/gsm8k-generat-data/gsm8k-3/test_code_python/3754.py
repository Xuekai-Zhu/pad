def solution():
    """A tiger shark has 180 teeth.  A hammerhead shark has 1/6 the number of teeth that a tiger shark has.  A great white shark has double the sum of teeth of a tiger shark and a hammerhead shark. How many teeth does a great white shark have?"""
    # Define the number of teeth of a tiger shark
    tiger_teeth = 180

    # Define the number of teeth of a hammerhead shark
    hammerhead_teeth = tiger_teeth / 6

    # Define the number of teeth of a great white shark
    great_white_teeth = 2 * (tiger_teeth + hammerhead_teeth)

    # Display the number of teeth of a great white shark
    result = great_white_teeth
    return result

print(solution())