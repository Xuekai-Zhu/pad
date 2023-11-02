def solution():
    # Calculate the number of fruits in the first three baskets
    fruits_in_first_3_baskets = 9 + 15 + 14

    # Calculate the number of fruits in the fourth basket
    apples_in_fourth_basket = 9 - 2
    oranges_in_fourth_basket = 15 - 2
    bananas_in_fourth_basket = 14 - 2
    fruits_in_fourth_basket = apples_in_fourth_basket + oranges_in_fourth_basket + bananas_in_fourth_basket

    # Calculate the total number of fruits in all the baskets
    total_fruits = fruits_in_first_3_baskets + fruits_in_fourth_basket
    result = total_fruits
    return result

print(solution())