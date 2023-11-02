def solution():
    # let's assume the number of green grapes as x
    x = 0
    # calculate the number of red grapes
    num_red_grapes = 3 * x + 7
    # calculate the number of raspberries
    num_raspberries = x - 5
    # calculate the total number of fruits in the salad
    total_fruits = x + num_red_grapes + num_raspberries
    # we know that total_fruits is 102
    # therefore x + 3x + 7 + x - 5 = 102
    # solving this equation we get x = 30
    num_red_grapes = 3 * x + 7
    result = num_red_grapes
    return result

print(solution())