def solution():
    # Calculate the area of the square-shaped street
    street_area = 100 * 100  # the street has a length of 100 meters on one side

    # Calculate the area of the forest
    forest_area = 3 * street_area  # the area of the forest is three times the area of the square-shaped street

    # Calculate the total number of trees in the forest
    trees_in_forest = forest_area * 4  # the number of trees per square meter in the forest is 4

    result = trees_in_forest
    return result

print(solution())