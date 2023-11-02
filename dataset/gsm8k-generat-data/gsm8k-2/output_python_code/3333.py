def solution():
    """On his farm, Mr. Mathews has goats and sheep in the ratio of 5:7. He decides to sell half of the goats at $40 each 
    and 2/3 of the sheep at $30 each. How much money does he make from the sale of the animals if the total number of 
    sheep and goats on the farm is 360?"""
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