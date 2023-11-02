def solution():
    """There are 56 pieces of fruit in a box. One-fourth of the box contains oranges. There are half as many peaches as oranges and five times as many apples as peaches. How many apples are in the box?"""
    total_fruits = 56
    oranges = total_fruits / 4
    peaches = oranges / 2
    apples = peaches * 5
    result = apples
    return result

print(solution())