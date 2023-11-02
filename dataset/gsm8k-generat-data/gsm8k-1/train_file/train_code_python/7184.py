def solution():
    """Avery has 20 chickens on his farm. Each chicken lays 6 eggs. He wants to fill up egg cartons with eggs. If each egg carton can hold a dozen (12 eggs), how many egg cartons can Avery fill?"""
    total_chicken_eggs = 20 * 6
    egg_carton_size = 12
    num_egg_cartons = total_chicken_eggs // egg_carton_size
    result = num_egg_cartons
    return result

print(solution())