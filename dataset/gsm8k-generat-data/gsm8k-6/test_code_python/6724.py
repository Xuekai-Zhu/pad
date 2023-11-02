def solution():
    # Calculate the number of fruits in the first three baskets
    fruits_first_three = 9 + 15 + 14  # apples, oranges, and bananas in the first three baskets

    # Calculate the number of fruits in the fourth basket
    apples_fourth = 9 - 2  # 2 less apples in the fourth basket
    oranges_fourth = 15 - 2  # 2 less oranges in the fourth basket
    bananas_fourth = 14 - 2  # 2 less bananas in the fourth basket
    fruits_fourth = apples_fourth + oranges_fourth + bananas_fourth  # number of fruits in the fourth basket

    # Calculate the total number of fruits in all the baskets
    total_fruits = fruits_first_three + fruits_fourth
    result = total_fruits
    return result

print(solution())