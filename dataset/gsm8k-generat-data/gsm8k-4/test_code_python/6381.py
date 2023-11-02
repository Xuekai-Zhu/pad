def solution():
    """The standard poodle is 8 inches taller than the miniature poodle, and the miniature poodle is 6 inches taller than the toy poodle. If the standard poodle in 28 inches tall, how tall is the toy poodle in inches?"""
    # Define the height difference between the standard poodle and the miniature poodle
    height_diff_standard_mini = 8

    # Define the height difference between the miniature poodle and the toy poodle
    height_diff_mini_toy = 6

    # Calculate the total height difference between the standard poodle and the toy poodle
    height_diff_standard_toy = height_diff_standard_mini + height_diff_mini_toy

    # Calculate the height of the toy poodle
    toy_poodle_height = 28 - height_diff_standard_toy

    # Return the result
    result = toy_poodle_height
    return result

print(solution())