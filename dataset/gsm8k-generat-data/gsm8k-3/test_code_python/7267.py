def solution():
    """James orders an 8 piece pizza.  His friend eats 2 slices and James eats half of what is left.  How many slices does James eat?"""
    # Define the total number of slices in the pizza
    total_slices = 8

    # Define the number of slices James' friend eats
    friend_slices = 2

    # Subtract the slices James' friend eats from the total
    remaining_slices = total_slices - friend_slices

    # Calculate the number of slices James eats
    james_slices = remaining_slices / 2

    # Display the number of slices James eats
    result = james_slices
    return result

print(solution())