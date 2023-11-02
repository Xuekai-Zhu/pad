def solution():
    park_length = 1000  # Park is 1000 feet long
    park_width = 2000  # Park is 2000 feet wide
    area_of_park = park_length * park_width  # Calculate the area of the park
    area_per_tree = 20  # There is 1 tree per 20 square feet

    # Calculate the total number of trees in the park
    total_trees = area_of_park / area_per_tree
    result = total_trees
    return result

print(solution())