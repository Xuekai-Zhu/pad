def solution():
    num_strawberry_plants = 5
    num_tomato_plants = 7

    strawberries_per_plant = 14
    tomatoes_per_plant = 16

    strawberries_per_basket = 7
    tomatoes_per_basket = 7

    strawberry_basket_price = 9
    tomato_basket_price = 6

    # Calculate the total number of strawberries harvested
    total_strawberries = num_strawberry_plants * strawberries_per_plant

    # Calculate the total number of tomatoes harvested
    total_tomatoes = num_tomato_plants * tomatoes_per_plant

    # Calculate the number of strawberry baskets and the revenue
    num_strawberry_baskets = total_strawberries / strawberries_per_basket
    strawberry_revenue = num_strawberry_baskets * strawberry_basket_price

    # Calculate the number of tomato baskets and the revenue
    num_tomato_baskets = total_tomatoes / tomatoes_per_basket
    tomato_revenue = num_tomato_baskets * tomato_basket_price

    # Calculate the total revenue
    total_revenue = strawberry_revenue + tomato_revenue
    result = total_revenue
    return result

print(solution())