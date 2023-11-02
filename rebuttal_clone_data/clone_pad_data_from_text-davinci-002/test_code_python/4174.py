def solution():
    red_boxcars = 3
    blue_boxcars = 4
    black_boxcars = 7
    coal_capacity_red = 4000 * 3
    coal_capacity_blue = 4000 / 2
    coal_capacity_black = 4000 * 2 / 3
    total_coal_capacity = (red_boxcars * coal_capacity_red) + (black_boxcars * coal_capacity_black) + (blue_boxcars * coal_capacity_blue)
    result = total_coal_capacity

    return result

print(solution())