def solution():
    """The area of a forest is three times the area of the square-shaped street. If the street has a length of 100 meters on one side and the number of trees per square meter in the forest is 4, calculate the total number of trees in the forest."""
    # Calculate the area of the square-shaped street
    street_area = 100**2

    # Calculate the area of the forest
    forest_area = 3 * street_area

    # Calculate the total number of trees in the forest
    tree_count = forest_area * 4

    # Display the total number of trees in the forest
    result = tree_count
    return result

print(solution())