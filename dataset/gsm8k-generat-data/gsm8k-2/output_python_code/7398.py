def solution():
    """There are six oranges in a fruit basket. There are two fewer apples than oranges. There are 3 times as many bananas as apples, and there are half as many peaches as bananas. How many pieces of fruit are in the fruit basket?"""
    oranges = 6
    apples = oranges - 2
    bananas = 3 * apples
    peaches = bananas / 2
    total_fruit = oranges + apples + bananas + peaches
    result = total_fruit
    return result

print(solution())