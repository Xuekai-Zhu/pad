def solution():
    """A pumpkin patch allows people to come pick pumpkins to carve in the fall every year. They charge $3 per person for a pumpkin. The remaining pumpkins get turned into cans of pie filling, 3 pumpkins to a can. They grew 83 pumpkins this year and made $96 selling pumpkins for carving. How many cans of pie filling will the pumpkin patch produce?"""
    pumpkins_grown = 83
    pumpkin_carving_sales = 96
    pumpkin_carving_price = 3
    pumpkins_carved = pumpkin_carving_sales // pumpkin_carving_price
    pumpkins_for_pie = pumpkins_grown - pumpkins_carved
    cans_of_pie_filling = pumpkins_for_pie // 3
    result = cans_of_pie_filling
    return result

print(solution())