def solution():
    """Jackie loves to climb trees.  She climbed a 1000 foot tall tree.  Then she climbed 2 trees that were half as tall as the first tree.  She finished by climbing a tree that was 200 feet taller than her first tree.  What was the average height of the trees that Jackie climbed?"""
    # Define the height of the first tree
    tree1_height = 1000

    # Calculate the height of the second tree
    tree2_height = tree1_height / 2

    # Calculate the height of the third tree
    tree3_height = tree1_height / 2

    # Calculate the height of the fourth tree
    tree4_height = tree1_height + 200

    # Calculate the total height of all the trees
    total_height = tree1_height + tree2_height + tree3_height + tree4_height

    # Calculate the average height of the trees
    avg_height = total_height / 4

    # Display the average height
    result = avg_height
    return result

print(solution())