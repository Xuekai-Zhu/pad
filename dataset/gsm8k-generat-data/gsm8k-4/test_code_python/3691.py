def solution():
    """Nathan planted 5 strawberry plants and 7 tomato plants. He harvested 14 strawberries from each plant and 16 tomatoes from each plant. He then distributed the strawberries and tomatoes into baskets of 7. He sold a basket of strawberries for $9 and a basket of tomatoes for $6. How much money does Nathan make from his harvest?"""
    # Define the number of strawberry and tomato plants
    strawberry_plants = 5
    tomato_plants = 7

    # Calculate the total number of strawberries and tomatoes harvested
    total_strawberries = strawberry_plants * 14
    total_tomatoes = tomato_plants * 16

    # Calculate the number of strawberry and tomato baskets
    strawberry_baskets = total_strawberries // 7
    tomato_baskets = total_tomatoes // 7

    # Calculate the total amount of money made from selling the baskets
    total_money = (strawberry_baskets * 9) + (tomato_baskets * 6)

    result = total_money
    return result

print(solution())