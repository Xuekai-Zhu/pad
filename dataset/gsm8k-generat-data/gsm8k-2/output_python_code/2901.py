def solution():
    """Dane’s two daughters need to plant 5 flowers each to grow a garden. As the days passed, the flowers grew into 20 more but 10 of them died. Dane’s daughters harvested the flowers and split them between 5 different baskets. How many flowers ended up in each basket?"""
    initial_flowers = 2 * 5
    grown_flowers = initial_flowers + 20
    dead_flowers = 10
    harvested_flowers = grown_flowers - dead_flowers
    baskets = 5
    flowers_per_basket = harvested_flowers // baskets
    result = flowers_per_basket
    return result

print(solution())