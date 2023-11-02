def solution():
    """Avery has 20 chickens on his farm. Each chicken lays 6 eggs. He wants to fill up egg cartons with eggs. If each egg carton can hold a dozen (12 eggs), how many egg cartons can Avery fill?"""
    # Define the number of chickens and eggs
    num_chickens = 20
    eggs_per_chicken = 6

    # Calculate the total number of eggs
    total_eggs = num_chickens * eggs_per_chicken

    # Calculate the number of egg cartons that can be filled
    egg_cartons = total_eggs // 12

    # return the result
    result = egg_cartons
    return result

print(solution())