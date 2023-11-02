def solution():
    
    current_dow = 8722
    percent_change = 2
    previous_dow = current_dow / (1 - percent_change/100)
    result = previous_dow
    return result

print(solution())