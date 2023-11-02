def solution():
    park_length = 1000
    park_width = 2000
    tree_density = 20

    # Calculate the area of the park
    park_area = park_length * park_width

    # Calculate the number of trees in the park based on tree density
    num_trees = park_area / tree_density
    result = num_trees
    return result

print(solution())