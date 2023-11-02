def solution():
    total_roses = 80
    red_roses = total_roses * (3/4)
    yellow_roses = (total_roses - red_roses) * (1/4)
    white_roses = total_roses - red_roses - yellow_roses
    result = red_roses + white_roses
    return result

print(solution())