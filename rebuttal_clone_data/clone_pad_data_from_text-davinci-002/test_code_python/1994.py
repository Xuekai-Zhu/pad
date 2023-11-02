def solution():
    oranges = 40
    apples = 70
    oranges_sold = oranges / 4
    apples_sold = apples / 2
    total_fruits_left = oranges + apples - oranges_sold - apples_sold
    result = total_fruits_left
    return result

print(solution())