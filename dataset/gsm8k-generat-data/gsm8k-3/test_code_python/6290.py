def solution():
    """There are three trees in the town square. The tallest tree is 150 feet tall. The middle height tree is 2/3 the height of the tallest tree. The shortest tree is half the size of the middle tree.  How tall is the shortest tree?"""
    # Define the height of the tallest tree
    tallest_tree = 150

    # Calculate the height of the middle tree
    middle_tree = tallest_tree * (2/3)

    # Calculate the height of the shortest tree
    shortest_tree = middle_tree * (1/2)

    # Display the height of the shortest tree
    result = shortest_tree
    return result

print(solution())