def solution():
    """The area of a forest is three times the area of the square-shaped street. If the street has a length of 100 meters on one side and the number of trees per square meter in the forest is 4, calculate the total number of trees in the forest."""
    street_area = 100**2
    forest_area = 3 * street_area
    trees_per_square_meter = 4
    total_trees = forest_area * trees_per_square_meter
    result = total_trees
    return result

print(solution())