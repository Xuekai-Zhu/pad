def solution():
    """Tom got 40 oranges and 70 apples. If he sold 1/4 of the oranges and 1/2 of the apples. How many fruits were left in total?"""
    oranges = 40
    apples = 70
    sold_oranges = oranges / 4
    sold_apples = apples / 2
    left_oranges = oranges - sold_oranges
    left_apples = apples - sold_apples
    total_left = left_oranges + left_apples
    result = total_left
    return result

print(solution())