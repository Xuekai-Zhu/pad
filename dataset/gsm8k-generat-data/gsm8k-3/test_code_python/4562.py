def solution():
    """Maynard's dog dug 8 holes in the lawn.  Maynard filled in 75% of the hole with dirt.  How many holes remain unfilled?"""
    # Define the number of holes dug by the dog
    num_holes = 8

    # Define the percentage of each hole that Maynard filled in with dirt
    fill_percentage = 0.75

    # Calculate the number of holes that remain unfilled
    unfilled_holes = num_holes - (num_holes * fill_percentage)

    # Display the number of holes that remain unfilled
    result = unfilled_holes
    return result

print(solution())