def solution():
    
    num_snakes = 3
    eggs_per_snake = 2
    total_eggs = num_snakes * eggs_per_snake
    normal_snake_price = 250
    rare_snake_price = 4 * normal_snake_price
    total_sales = (total_eggs - 1) * normal_snake_price + rare_snake_price
    result = total_sales
    return result

print(solution())