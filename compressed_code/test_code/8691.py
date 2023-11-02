def solution():
    
    pumpkins_grown = 83
    pumpkin_carving_sales = 96
    pumpkin_carving_price = 3
    pumpkins_carved = pumpkin_carving_sales // pumpkin_carving_price
    pumpkins_for_pie = pumpkins_grown - pumpkins_carved
    cans_of_pie_filling = pumpkins_for_pie // 3
    result = cans_of_pie_filling
    return result

print(solution())