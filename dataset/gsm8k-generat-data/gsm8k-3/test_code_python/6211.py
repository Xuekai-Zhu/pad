def solution():
    """Jane is looking at a tree. At the same time, the tree and Jane are casting shadows - the tree of 10 meters and Jane of 0.5 meters. Jane is 1.5 meters tall. How tall is the tree?"""
    # Define the lengths of Jane's shadow and the tree's shadow
    jane_shadow = 0.5
    tree_shadow = 10.0

    # Define Jane's height
    jane_height = 1.5

    # Calculate the height of the tree
    tree_height = (jane_height / jane_shadow) * tree_shadow

    # Display the height of the tree
    result = tree_height
    return result

print(solution())