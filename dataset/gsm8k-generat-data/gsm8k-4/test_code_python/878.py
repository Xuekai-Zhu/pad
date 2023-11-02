def solution():
    """Santino has 2 papaya trees and 3 mango trees. If each papaya tree produces 10 papayas and each mango tree produces 20 mangos, how many fruits does Santino have in total?"""
    # Define the number of trees and fruits per tree
    PAPAYA_TREES = 2
    PAPAYA_FRUITS_PER_TREE = 10

    MANGO_TREES = 3
    MANGO_FRUITS_PER_TREE = 20

    # Calculate the total number of fruits
    total_papayas = PAPAYA_TREES * PAPAYA_FRUITS_PER_TREE
    total_mangos = MANGO_TREES * MANGO_FRUITS_PER_TREE

    total_fruits = total_papayas + total_mangos

    # return the result
    result = total_fruits
    return result

print(solution())