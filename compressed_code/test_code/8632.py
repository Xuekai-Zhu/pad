def solution():
    
    mangoes = 400
    apples = mangoes * 2
    oranges = mangoes + 200
    total_produce = mangoes + apples + oranges
    price_per_kg = 50
    total_money = total_produce * price_per_kg
    
    return total_money

print(solution())