def solution():
    total_plants = 80  # Lydia has 80 plants
    flowering_plants = 0.4 * total_plants  # 40% of her plants are flowering plants
    plants_on_porch = flowering_plants / 4  # Lydia wants to place a fourth of her flowering plants on the porch
    flowers_on_porch = plants_on_porch * 5  # Each flowering plant produces 5 flowers

    result = flowers_on_porch
    return result

print(solution())