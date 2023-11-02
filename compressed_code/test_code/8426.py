def solution():
    
    ratio = 5/7
    total_animals = 360
    goats = total_animals * ratio * 2
    sheep = total_animals - goats
    goat_sell_price = 40
    sheep_sell_price = 30
    goat_sell_count = goats / 2
    sheep_sell_count = (2/3) * sheep
    total_goat_sale = goat_sell_count * goat_sell_price
    total_sheep_sale = sheep_sell_count * sheep_sell_price
    total_sale = total_goat_sale + total_sheep_sale
    return total_sale

print(solution())