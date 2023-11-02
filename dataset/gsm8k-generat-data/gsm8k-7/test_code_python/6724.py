def solution():
    num_baskets = 4
    num_apples = 9
    num_oranges = 15
    num_bananas = 14

    # Calculate the number of fruits in the first three baskets
    total_fruits_first_three = num_apples + num_oranges + num_bananas

    # Calculate the number of fruits in the fourth basket
    num_apples_fourth = num_apples - 2
    num_oranges_fourth = num_oranges - 2
    num_bananas_fourth = num_bananas - 2

    # Calculate the total number of fruits in all four baskets
    total_fruits = total_fruits_first_three + num_apples_fourth + num_oranges_fourth + num_bananas_fourth
    result = total_fruits
    return result

print(solution())