def solution():
    """There is a fruit display that has apples, oranges, and bananas. There are twice as many apples as oranges, and there are twice as many oranges as bananas. How many fruits are on the display in total if there are 5 bananas on the display?"""
    bananas = 5
    oranges = bananas * 2
    apples = oranges * 2
    total_fruits = bananas + oranges + apples
    result = total_fruits
    return result

print(solution())