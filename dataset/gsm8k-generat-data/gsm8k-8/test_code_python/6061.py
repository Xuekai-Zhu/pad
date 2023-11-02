def solution():
    # Define the number of red marbles and the ratio of blue to red marbles
    red_marbles = 14
    blue_red_ratio = 3
    
    # Calculate the number of blue marbles
    blue_marbles = blue_red_ratio * red_marbles

    # Calculate the total number of blue and red marbles
    total_blue_red = blue_marbles + red_marbles

    # Calculate the number of yellow marbles
    yellow_marbles = 85 - total_blue_red

    result = yellow_marbles
    return result

print(solution())