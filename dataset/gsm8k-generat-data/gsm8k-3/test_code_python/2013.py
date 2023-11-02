def solution():
    """There are 120 crayons in a box.  One third of the crayons are new, 20% are broken, and the rest are slightly used.  How many are slightly used?"""
    # Define the number of crayons in the box
    CRAYON_COUNT = 120

    # Calculate the number of new crayons
    new_crayon_count = CRAYON_COUNT // 3

    # Calculate the number of broken crayons
    broken_crayon_count = CRAYON_COUNT * 0.2

    # Calculate the number of slightly used crayons
    slightly_used_crayon_count = CRAYON_COUNT - new_crayon_count - broken_crayon_count

    # Display the number of slightly used crayons
    result = slightly_used_crayon_count
    return result

print(solution())