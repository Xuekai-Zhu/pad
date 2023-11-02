def solution():
    
    strawberry_plants = 5
    tomato_plants = 7
    strawberries_per_plant = 14
    tomatoes_per_plant = 16
    strawberries_harvested = strawberry_plants * strawberries_per_plant
    tomatoes_harvested = tomato_plants * tomatoes_per_plant
    total_baskets_strawberries = strawberries_harvested // 7
    total_baskets_tomatoes = tomatoes_harvested // 7
    price_per_basket_strawberries = 9
    price_per_basket_tomatoes = 6
    total_money = (total_baskets_strawberries * price_per_basket_strawberries) + (total_baskets_tomatoes * price_per_basket_tomatoes)
    result = total_money
    return result

print(solution())