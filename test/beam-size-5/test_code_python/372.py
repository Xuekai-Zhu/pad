def solution():
    
    total_pupils = 40
    blue_pupils = total_pupils / 2
    remaining_pupils = total_pupils - blue_pupils
    green_pupils = remaining_pupils / 4
    yellow_pupils = remaining_pupils - green_pupils
    result = yellow_pupils
    return result

print(solution())