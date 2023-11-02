def solution():
    # Calculate the total volume of the iron bars
    iron_bar_volume = 12 * 8 * 6 * 10

    # Calculate the number of iron balls that can be molded
    num_balls = iron_bar_volume // 8
    result = num_balls
    return result

print(solution())