def solution():
    
    total_trees = 110 * 3
    gabriela_oranges = 600 * 110
    alba_oranges = 400 * 110
    maricela_oranges = 500 * 110
    total_oranges = gabriela_oranges + alba_oranges + maricela_oranges
    total_cups_of_juice = total_oranges // 3
    total_sales = total_cups_of_juice * 4

    result = total_sales
    return result

print(solution())