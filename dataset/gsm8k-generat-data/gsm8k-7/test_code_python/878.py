def solution():
    num_papaya_trees = 2
    num_mango_trees = 3
    papaya_per_tree = 10
    mango_per_tree = 20

    # Calculate the total number of papayas
    total_papayas = num_papaya_trees * papaya_per_tree

    # Calculate the total number of mangos
    total_mangos = num_mango_trees * mango_per_tree

    # Calculate the total number of fruits
    total_fruits = total_papayas + total_mangos
    result = total_fruits
    return result

print(solution())