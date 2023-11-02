def solution():
    # Calculate the total volume of the iron bars
    bar_volume = 12 * 8 * 6  # Length x Width x Height

    # Calculate the total number of iron balls that can be molded
    num_balls = bar_volume / 8  # Each ball has a volume of 8 cubic cm

    # Calculate the number of iron bars multiplied by the number of iron balls molded
    total_num_balls = 10 * num_balls

    result = total_num_balls
    return result

print(solution())