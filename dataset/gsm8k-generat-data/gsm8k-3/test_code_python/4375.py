def solution():
    """A quarterback throws 50 passes in one game.  He throws twice as many passes to the right of the field than he does to the left of the field.  He throws 2 more passes to the center of the field than he did to the left.  How many passes did he throw to the left side of the field?"""
    # Define the number of passes to the left, right, and center of the field
    passes_left = x # unknown
    passes_right = passes_left * 2
    passes_center = passes_left + 2

    # Calculate the total number of passes
    total_passes = passes_left + passes_right + passes_center

    # Use the fact that the total number of passes is 50 to solve for passes_left
    passes_left = (50 - passes_center - passes_right) / 2

    # Display the number of passes thrown to the left side of the field
    result = passes_left
    return result

print(solution())