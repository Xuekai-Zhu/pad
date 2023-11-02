def solution():
    percent_red = 40
    percent_green = 30
    percent_white = 100 - percent_red - percent_green
    num_red = 20
    num_white = num_red * (percent_white / percent_red)
    result = num_white
    return result

print(solution())