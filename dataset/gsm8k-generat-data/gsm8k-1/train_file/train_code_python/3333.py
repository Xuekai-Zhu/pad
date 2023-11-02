def solution():
    """On his farm, Mr. Mathews has goats and sheep in the ratio of 5:7. He decides to sell half of the goats at $40 each and 2/3 of the sheep at $30 each. How much money does he make from the sale of the animals if the total number of sheep and goats on the farm is 360?"""
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