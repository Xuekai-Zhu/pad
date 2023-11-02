def solution():
    # Calculate the area of the square-shaped street
    street_area = 100 * 100

    # Calculate the area of the forest
    forest_area = 3 * street_area

    # Calculate the total number of trees in the forest
    trees_per_sq_meter = 4
    total_trees = forest_area * trees_per_sq_meter
    result = total_trees
    return result

print(solution())