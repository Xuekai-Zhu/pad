def solution():
    """Jackie loves to climb trees. She climbed a 1000 foot tall tree. Then she climbed 2 trees that were half as tall as the first tree. She finished by climbing a tree that was 200 feet taller than her first tree. What was the average height of the trees that Jackie climbed?"""
    # Define the height of the first tree
    first_tree = 1000

    # Calculate the heights of the second and third trees
    second_tree = first_tree / 2
    third_tree = first_tree + 200

    # Calculate the total height of all the trees
    total_height = first_tree + second_tree + second_tree + third_tree

    # Calculate the average height of the trees
    average_height = total_height / 4

    # Return the result
    result = average_height
    return result

print(solution())