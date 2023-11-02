def solution():
    papaya_trees = 2
    mango_trees = 3
    papayas_per_tree = 10
    mangos_per_tree = 20

    # Calculate the total number of papayas
    total_papayas = papaya_trees * papayas_per_tree

    # Calculate the total number of mangos
    total_mangos = mango_trees * mangos_per_tree

    # Calculate the total number of fruits
    total_fruits = total_papayas + total_mangos
    result = total_fruits
    return result

print(solution())