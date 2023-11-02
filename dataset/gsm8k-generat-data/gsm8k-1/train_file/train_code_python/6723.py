def solution():
    """A group of 4 fruit baskets contains 9 apples, 15 oranges, and 14 bananas in the first three baskets and 2 less of each fruit in the fourth basket. How many fruits are there?"""
    num_baskets = 4
    apples_first_3_baskets = 9
    oranges_first_3_baskets = 15
    bananas_first_3_baskets = 14
    apples_fourth_basket = apples_first_3_baskets - 2
    oranges_fourth_basket = oranges_first_3_baskets - 2
    bananas_fourth_basket = bananas_first_3_baskets - 2
    total_fruits = (apples_first_3_baskets + oranges_first_3_baskets + bananas_first_3_baskets) * 3 + (apples_fourth_basket + oranges_fourth_basket + bananas_fourth_basket)
    result = total_fruits
    return result

print(solution())