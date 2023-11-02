def solution():
    amount_planted_strawberry = 5
    amount_planted_tomato = 7
    amount_harvested_strawberry = 14
    amount_harvested_tomato = 16
    strawberry_baskets = amount_harvested_strawberry / 7
    tomato_baskets = amount_harvested_tomato / 7
    money_made_strawberry = strawberry_baskets * 9
    money_made_tomato = tomato_baskets * 6
    money_made_total = money_made_strawberry + money_made_tomato
    result = money_made_total
    
    return result

print(solution())