def solution():
    """The standard poodle is 8 inches taller than the miniature poodle, and the miniature poodle is 6 inches taller than the toy poodle.  If the standard poodle in 28 inches tall, how tall is the toy poodle in inches?"""
    # Define the height difference between the standard and miniature poodle
    STANDARD_TO_MINI_DIFF = 8

    # Define the height difference between the miniature and toy poodle
    MINI_TO_TOY_DIFF = 6

    # Calculate the height of the miniature poodle
    mini_height = 28 - STANDARD_TO_MINI_DIFF

    # Calculate the height of the toy poodle
    toy_height = mini_height - MINI_TO_TOY_DIFF

    # Display the height of the toy poodle
    result = toy_height
    return result

print(solution())