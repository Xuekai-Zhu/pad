def solution():
    
    total_caps = 125
    red_caps = 50
    green_caps = total_caps - red_caps
    green_percentage = (green_caps / total_caps) * 100
    result = green_percentage
    return result

print(solution())