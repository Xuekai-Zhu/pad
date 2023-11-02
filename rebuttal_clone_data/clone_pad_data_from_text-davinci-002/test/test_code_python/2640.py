def solution():
    apples_bought = 14
    oranges_bought = 9
    blueberries_bought = 6
    apples_eaten = 1
    oranges_eaten = 1
    blueberries_eaten = 1
    apples_left = apples_bought - apples_eaten
    oranges_left = oranges_bought - oranges_eaten
    blueberries_left = blueberries_bought - blueberries_eaten
    total_left = apples_left + oranges_left + blueberries_left
    result = total_left
    return result

print(solution())