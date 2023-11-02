def solution():
    """An iron bar measures 12 cm by 8 cm by  6 cm. A factory wants to melt ten iron bars and mold them into iron balls. Each iron ball has a volume of 8 cubic cm. How many iron balls have been molded?"""
    # Define the dimensions of the iron bar and the number of bars
    length = 12
    width = 8
    height = 6
    num_bars = 10

    # Calculate the volume of each iron bar
    bar_volume = length * width * height

    # Calculate the total volume of all the iron bars
    total_volume = bar_volume * num_bars

    # Calculate the number of iron balls that can be molded with the total volume
    num_balls = total_volume / 8

    # Round down to the nearest integer to get the number of iron balls that can be molded
    num_balls = int(num_balls)

    result = num_balls
    return result

print(solution())