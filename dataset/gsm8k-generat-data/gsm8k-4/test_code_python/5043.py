def solution():
    """The area of a forest is three times the area of the square-shaped street. If the street has a length of 100 meters on one side and the number of trees per square meter in the forest is 4, calculate the total number of trees in the forest."""
    # Define the length of one side of the square-shaped street
    street_length = 100

    # Calculate the area of the square-shaped street
    street_area = street_length ** 2

    # Calculate the area of the forest
    forest_area = street_area * 3

    # Calculate the total number of trees in the forest, given that there are 4 trees per square meter
    total_trees = forest_area * 4

    result = total_trees
    return result

print(solution())