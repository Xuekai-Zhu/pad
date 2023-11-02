def solution():
    """A group of 4 fruit baskets contains 9 apples, 15 oranges, and 14 bananas in the first three baskets and 2 less of each fruit in the fourth basket. How many fruits are there?"""
    apples = 9 + 9 + 9 + (9-2)
    oranges = 15 + 15 + 15 + (15-2)
    bananas = 14 + 14 + 14 + (14-2)
    total_fruits = apples + oranges + bananas
    result = total_fruits
    return result

print(solution())