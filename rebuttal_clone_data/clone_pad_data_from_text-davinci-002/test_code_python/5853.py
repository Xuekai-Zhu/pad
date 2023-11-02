def solution():
    green_grapes = 3
    red_grapes = green_grapes * 7
    raspberries = green_grapes - 5
    total_fruit = 102
    total_red_grapes = total_fruit - (green_grapes + raspberries)
    result = total_red_grapes
    return result

print(solution())