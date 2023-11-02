def solution():
    
    num_trees = 110
    gabriela_oranges = 600
    alba_oranges = 400
    maricela_oranges = 500
    total_oranges = num_trees * (gabriela_oranges + alba_oranges + maricela_oranges)
    cups_of_juice = total_oranges / 3
    price_per_cup = 4
    revenue = cups_of_juice * price_per_cup
    result = revenue
    return result

print(solution())