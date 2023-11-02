def solution():
    """A group of 4 fruit baskets contains 9 apples, 15 oranges, and 14 bananas in the first three baskets and 2 less of each fruit in the fourth basket. How many fruits are there?"""
    # Define the number of fruits in the first three baskets
    apples_1 = 9
    oranges_1 = 15
    bananas_1 = 14

    # Define the number of fruits in the fourth basket
    apples_4 = apples_1 - 2
    oranges_4 = oranges_1 - 2
    bananas_4 = bananas_1 - 2

    # Calculate the total number of fruits
    total_apples = apples_1 * 3 + apples_4
    total_oranges = oranges_1 * 3 + oranges_4
    total_bananas = bananas_1 * 3 + bananas_4

    total_fruits = total_apples + total_oranges + total_bananas

    # return the result
    result = total_fruits
    return result

print(solution())