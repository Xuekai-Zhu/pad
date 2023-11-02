def solution():
    """Carson needs to mow the lawn and plant some flowers. Carson has to mow 40 lines to cover the whole yard, and it takes him 2 minutes to mow one line. He also needs to plant 8 rows of flowers, each with 7 flowers, and it takes him half a minute to plant each flower. How many minutes will Carson spend gardening?"""
    mowing_lines = 40
    mowing_time_per_line = 2
    total_mowing_time = mowing_lines * mowing_time_per_line
    flower_rows = 8
    flowers_per_row = 7
    flower_time_per_flower = 0.5
    total_flower_time = flower_rows * flowers_per_row * flower_time_per_flower
    total_gardening_time = total_mowing_time + total_flower_time
    result = total_gardening_time
    return result

print(solution())