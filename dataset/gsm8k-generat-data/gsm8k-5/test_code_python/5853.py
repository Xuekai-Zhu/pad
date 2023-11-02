def solution():
    # Let's say there are x green grapes
    x = 0

    # There are 7 more than 3 times the number of red grapes as green grapes
    # So the number of red grapes is (3x + 7)
    red_grapes = 3 * x + 7

    # There are 5 less raspberries than green grapes
    raspberries = x - 5

    # The total number of fruit in the salad is 102
    total_fruit = red_grapes + raspberries + x

    # We can set up an equation to solve for x
    # x + (3x + 7) + (x - 5) = 102
    # 5x + 2 = 102
    # 5x = 100
    # x = 20

    # Now that we know x, we can calculate the number of red grapes
    red_grapes = 3 * x + 7
    result = red_grapes
    return result

print(solution())