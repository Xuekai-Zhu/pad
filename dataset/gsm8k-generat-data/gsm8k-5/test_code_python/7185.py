def solution():
    chickens = 20  # Avery has 20 chickens
    eggs_per_chicken = 6  # Each chicken lays 6 eggs

    # Total number of eggs laid by all the chickens
    total_eggs = chickens * eggs_per_chicken

    # Number of egg cartons that can be filled
    egg_cartons = total_eggs // 12

    result = egg_cartons
    return result

print(solution())