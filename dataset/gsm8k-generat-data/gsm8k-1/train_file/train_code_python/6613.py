def solution():
    """Jake has 3 snakes. Each of them lays 2 eggs. Most of the baby snakes sell for $250 but one super rare one costs 4 times as much. How much did he get from selling the snakes?"""
    num_snakes = 3
    eggs_per_snake = 2
    total_eggs = num_snakes * eggs_per_snake
    rare_snake_price = 4 * 250
    total_sales = (total_eggs - 1) * 250 + rare_snake_price
    result = total_sales
    return result

print(solution())