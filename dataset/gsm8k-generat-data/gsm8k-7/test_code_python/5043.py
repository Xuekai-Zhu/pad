def solution():
    street_area = 100 * 100  # area of the square-shaped street
    forest_area = 3 * street_area  # area of the forest

    num_trees_per_square_meter = 4

    total_num_trees = num_trees_per_square_meter * forest_area  # calculate total number of trees
    result = total_num_trees
    return result

print(solution())