def solution():
    blue_ratio = 0.5
    red_ratio = 0.25
    green_num = 27
    yellow_num = 14

    # Calculate the total ratio of non-green marbles
    non_green_ratio = blue_ratio + red_ratio

    # Calculate the total number of non-green marbles
    non_green_num = (1 - green_num / (non_green_ratio)) * non_green_ratio

    # Calculate the total number of marbles
    total_num = non_green_num + green_num + yellow_num
    result = total_num
    return result

print(solution())