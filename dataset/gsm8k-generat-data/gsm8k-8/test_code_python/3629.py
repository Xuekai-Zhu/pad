def solution():
    total_roses = 80
    red_roses = (3/4) * total_roses
    remaining_roses = total_roses - red_roses
    yellow_roses = (1/4) * remaining_roses
    white_roses = remaining_roses - yellow_roses
    red_or_white_roses = red_roses + white_roses
    result = red_or_white_roses
    return result

print(solution())