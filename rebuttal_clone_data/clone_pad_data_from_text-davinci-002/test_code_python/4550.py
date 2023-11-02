def solution():
    money_earned_1 = 30
    money_earned_2 = 24
    money_earned_3 = 42
    price_per_kg = 2
    kg_sold_1 = money_earned_1 / price_per_kg
    kg_sold_2 = money_earned_2 / price_per_kg
    kg_sold_3 = money_earned_3 / price_per_kg
    total_kg_sold = kg_sold_1 + kg_sold_2 + kg_sold_3
    result = total_kg_sold
    return result

print(solution())