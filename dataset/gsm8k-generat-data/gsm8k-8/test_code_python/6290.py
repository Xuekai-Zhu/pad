def solution():
    # Define the height of the tallest tree
    tallest_tree = 150

    # Calculate the height of the middle tree
    middle_tree = tallest_tree * (2/3)

    # Calculate the height of the shortest tree
    shortest_tree = middle_tree * 0.5

    result = shortest_tree
    return result

print(solution())