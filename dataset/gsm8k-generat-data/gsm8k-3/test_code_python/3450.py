def solution():
    """Carson needs to mow the lawn and plant some flowers. Carson has to mow 40 lines to cover the whole yard, and it takes him 2 minutes to mow one line. He also needs to plant 8 rows of flowers, each with 7 flowers, and it takes him half a minute to plant each flower. How many minutes will Carson spend gardening?"""
    # Calculate the time required to mow the lawn
    mow_lines = 40
    time_per_line = 2 # minutes
    mow_time = mow_lines * time_per_line

    # Calculate the time required to plant the flowers
    rows = 8
    flowers_per_row = 7
    time_per_flower = 0.5 # minutes
    flower_time = rows * flowers_per_row * time_per_flower

    # Calculate the total time Carson will spend gardening
    total_time = mow_time + flower_time

    # Display the total time
    result = total_time
    return result

print(solution())