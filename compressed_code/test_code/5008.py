def solution():
    
    total_mugs = 40
    total_colors = 4
    yellow_mugs = 12
    red_mugs = yellow_mugs / 2
    blue_mugs = 3 * red_mugs
    total_colored_mugs = yellow_mugs + red_mugs + blue_mugs
    other_mugs = total_mugs - total_colored_mugs
    result = other_mugs
    return result

print(solution())