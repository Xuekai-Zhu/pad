def solution():
    """Avery has 20 chickens on his farm. Each chicken lays 6 eggs. He wants to fill up egg cartons with eggs. If each egg carton can hold a dozen (12 eggs), how many egg cartons can Avery fill?"""
    total_eggs = 20 * 6
    cartons = total_eggs // 12
    result = cartons
    return result

print(solution())