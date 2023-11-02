def solution():
    """James orders an 8 piece pizza. His friend eats 2 slices and James eats half of what is left. How many slices does James eat?"""
    # Define the total number of slices in the pizza
    total_slices = 8

    # Calculate the number of slices eaten by James' friend
    friend_slices = 2

    # Calculate the remaining slices after James' friend eats
    remaining_slices = total_slices - friend_slices

    # Calculate the number of slices eaten by James
    james_slices = remaining_slices / 2

    result = james_slices
    return result

print(solution())