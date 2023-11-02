def solution():
    """A family bought 1 box of pizza that is cut into 16 slices. Only three-fourths of the pizza was eaten by the family. How many slices of pizza were left?"""
    # Define the number of slices in one box of pizza
    slices_per_box = 16

    # Calculate the number of slices eaten by the family
    slices_eaten = slices_per_box * (3/4)

    # Calculate the number of slices left
    slices_left = slices_per_box - slices_eaten

    # Display the number of slices left
    result = slices_left
    return result

print(solution())