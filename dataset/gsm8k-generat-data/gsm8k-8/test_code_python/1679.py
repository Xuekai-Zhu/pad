def solution():
    park_area = 1000 * 2000  # Calculate the area of the park
    tree_density = 1 / 20  # Calculate the tree density per square foot
    tree_count = park_area * tree_density  # Calculate the total number of trees in the park
    result = tree_count
    return result

print(solution())