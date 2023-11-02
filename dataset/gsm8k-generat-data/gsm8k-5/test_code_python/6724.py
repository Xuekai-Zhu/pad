def solution():
    # Total number of apples, oranges, and bananas in the first three baskets
    total_fruits_first_three = 9 + 15 + 14

    # Number of each fruit in the fourth basket
    apples_fourth_basket = 9 - 2
    oranges_fourth_basket = 15 - 2
    bananas_fourth_basket = 14 - 2

    # Total number of fruits in all four baskets
    total_fruits = total_fruits_first_three + apples_fourth_basket + oranges_fourth_basket + bananas_fourth_basket
    result = total_fruits
    return result

print(solution())