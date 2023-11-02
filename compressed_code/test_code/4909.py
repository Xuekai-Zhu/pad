def solution():
    
    green_houses = 90
    yellow_houses = green_houses / 3
    red_houses = yellow_houses + 40
    total_houses = green_houses + yellow_houses + red_houses
    not_yellow_houses = total_houses - yellow_houses
    result = not_yellow_houses
    return result

print(solution())