def solution():
    total_flowers = 96
    num_green = 9
    num_red = 3 * num_green
    num_blue = total_flowers // 2
    
    # Calculate the number of yellow flowers
    num_yellow = total_flowers - num_green - num_red - num_blue
    result = num_yellow
    return result

print(solution())