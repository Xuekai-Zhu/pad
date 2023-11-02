def solution():
    """Nathan planted 5 strawberry plants and 7 tomato plants. He harvested 14 strawberries from each plant and 16 tomatoes from each plant. He then distributed the strawberries and tomatoes into baskets of 7. He sold a basket of strawberries for $9 and a basket of tomatoes for $6. How much money does Nathan make from his harvest?"""
    # Define the number of plants and number of fruits each plant produced
    STRAWBERRY_PLANTS = 5
    STRAWBERRIES_PER_PLANT = 14
    TOMATO_PLANTS = 7
    TOMATOES_PER_PLANT = 16

    # Calculate the total number of fruits
    total_strawberries = STRAWBERRY_PLANTS * STRAWBERRIES_PER_PLANT
    total_tomatoes = TOMATO_PLANTS * TOMATOES_PER_PLANT

    # Calculate the number of baskets of strawberries and tomatoes
    strawberry_baskets = total_strawberries // 7
    tomato_baskets = total_tomatoes // 7

    # Calculate Nathan's earnings
    earnings = (strawberry_baskets * 9) + (tomato_baskets * 6)

    # Display Nathan's earnings
    result = earnings
    return result

print(solution())