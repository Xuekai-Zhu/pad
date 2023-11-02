def solution():
    total_trees = 110
    oranges_per_tree_gabriela = 600
    oranges_per_tree_alba = 400
    oranges_per_tree_maricela = 500
    total_oranges = total_trees * (oranges_per_tree_gabriela + oranges_per_tree_alba + oranges_per_tree_maricela)
    oranges_needed_for_1_cup_of_juice = 3
    total_cups_of_juice = total_oranges / oranges_needed_for_1_cup_of_juice
    price_per_cup = 4
    total_revenue = total_cups_of_juice * price_per_cup
    result = total_revenue
    return result

print(solution())