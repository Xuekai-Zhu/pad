def solution():
    # Calculate the total number of trees to be planted
    total_trees = 18 * 2
    # Calculate the number of fruit trees to be planted
    fruit_trees = total_trees // 2
    # Calculate the number of each kind of fruit tree to be planted
    num_of_each = fruit_trees // 3
    result = f"{num_of_each} plum trees, {num_of_each} pear trees, and {num_of_each} apricot trees"
    return result

print(solution())