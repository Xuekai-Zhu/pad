def solution():
    trees_per_grove = 110  # Each sister owns a grove with 110 trees
    oranges_per_tree_gabriela = 600  # Gabriela's grove produces 600 oranges per tree
    oranges_per_tree_alba = 400  # Alba's grove produces 400 oranges per tree
    oranges_per_tree_maricela = 500  # Maricela's grove produces 500 oranges per tree

    # Calculate the total number of oranges produced by each sister's grove
    total_oranges_gabriela = oranges_per_tree_gabriela * trees_per_grove
    total_oranges_alba = oranges_per_tree_alba * trees_per_grove
    total_oranges_maricela = oranges_per_tree_maricela * trees_per_grove

    # Calculate the total number of cups of juice the sisters can make
    total_cups_juice = (total_oranges_gabriela + total_oranges_alba + total_oranges_maricela) / 3

    # Calculate the total amount of money the sisters can make selling the juice
    total_money = total_cups_juice * 4
    result = total_money
    return result

print(solution())