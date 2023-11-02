def solution():
    # Find the number of red roses
    red_roses = (3/4) * 80

    # Find the number of roses that are not red
    not_red_roses = 80 - red_roses

    # Find the number of yellow roses
    yellow_roses = (1/4) * not_red_roses

    # Find the number of white roses
    white_roses = not_red_roses - yellow_roses

    # Calculate the total number of red and white roses
    total_red_white_roses = red_roses + white_roses

    result = total_red_white_roses
    return result

print(solution())