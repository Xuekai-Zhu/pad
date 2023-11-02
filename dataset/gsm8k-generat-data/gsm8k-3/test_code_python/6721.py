def solution():
    """The height of the tree in Kilmer Park is 52 feet. Each year it grows 5 feet. In 8 years, what will the height of the tree be in inches, assuming 1 foot is 12 inches."""
    # Define the initial height of the tree and the growth rate
    initial_height = 52
    growth_rate = 5

    # Calculate the height of the tree after 8 years
    final_height = initial_height + (growth_rate * 8)

    # Convert the height to inches
    height_inches = final_height * 12

    # Display the height in inches
    result = height_inches
    return result

print(solution())