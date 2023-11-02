def solution():
    # Calculate the height of the first tree
    first_tree = 1000
    # Calculate the heights of the second and third trees
    second_tree = first_tree / 2
    third_tree = first_tree / 2
    # Calculate the height of the fourth tree
    fourth_tree = first_tree + 200
    # Calculate the total height of all trees climbed
    total_height = first_tree + second_tree + third_tree + fourth_tree
    # Calculate the average height of trees climbed
    average_height = total_height / 4
    result = average_height
    return result

print(solution())