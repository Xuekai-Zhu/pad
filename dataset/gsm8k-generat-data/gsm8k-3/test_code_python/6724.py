def solution():
    """A group of 4 fruit baskets contains 9 apples, 15 oranges, and 14 bananas in the first three baskets and 2 less of each fruit in the fourth basket. How many fruits are there?"""
    # Calculate the number of fruits in the first three baskets
    total_fruits_first_three = 9 + 15 + 14

    # Calculate the number of fruits in the fourth basket
    apples = 9 - 2
    oranges = 15 - 2
    bananas = 14 - 2
    total_fruits_fourth = apples + oranges + bananas

    # Calculate the total number of fruits
    total_fruits = total_fruits_first_three + total_fruits_fourth

    # Display the total number of fruits
    result = total_fruits
    return result

print(solution())