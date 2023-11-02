def solution():
    trees_per_grove = 110
    oranges_per_tree_gabriela = 600
    oranges_per_tree_alba = 400
    oranges_per_tree_maricela = 500

    total_oranges_gabriela = trees_per_grove * oranges_per_tree_gabriela
    total_oranges_alba = trees_per_grove * oranges_per_tree_alba
    total_oranges_maricela = trees_per_grove * oranges_per_tree_maricela

    total_cups = (total_oranges_gabriela + total_oranges_alba + total_oranges_maricela) / 3
    cups_sold = total_cups / 3
    total_revenue = cups_sold * 4

    return total_revenue

print(solution())