def solution():
    """Santino has 2 papaya trees and 3 mango trees. If each papaya tree produces 10 papayas and each mango tree produces 20 mangos, how many fruits does Santino have in total?"""
    papaya_trees = 2
    mango_trees = 3
    papayas_per_tree = 10
    mangos_per_tree = 20
    total_papayas = papaya_trees * papayas_per_tree
    total_mangos = mango_trees * mangos_per_tree
    total_fruits = total_papayas + total_mangos
    result = total_fruits
    return result

print(solution())