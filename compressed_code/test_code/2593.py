def solution():
    
    total_animals = 360
    goat_ratio = 5
    sheep_ratio = 7
    goat_count = total_animals * goat_ratio / (goat_ratio + sheep_ratio)
    sheep_count = total_animals * sheep_ratio / (goat_ratio + sheep_ratio)
    goat_sale_count = goat_count / 2
    sheep_sale_count = sheep_count * 2 / 3
    total_sale_proceeds = (goat_sale_count * 40) + (sheep_sale_count * 30)
    result = total_sale_proceeds
    return result

print(solution())