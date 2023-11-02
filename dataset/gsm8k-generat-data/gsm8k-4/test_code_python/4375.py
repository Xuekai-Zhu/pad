def solution():
    """A quarterback throws 50 passes in one game. He throws twice as many passes to the right of the field than he does to the left of the field. He throws 2 more passes to the center of the field than he did to the left. How many passes did he throw to the left side of the field?"""
    # Define the total number of passes and the number of passes to the left
    total_passes = 50
    left_passes = None

    # Calculate the number of passes to the right
    right_passes = 2 * left_passes

    # Calculate the number of passes to the center
    center_passes = left_passes + 2

    # Calculate the total number of passes
    total_passes = left_passes + right_passes + center_passes

    # Set up an equation to solve for left_passes
    # left_passes + 2 * left_passes + (left_passes + 2) = 50
    # Simplify and solve for left_passes
    left_passes = (50 - 2 - 2) / 3

    # Round the result and return it
    result = round(left_passes)
    return result

print(solution())