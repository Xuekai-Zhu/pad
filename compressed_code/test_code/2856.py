def solution():
    
    white_wash_time = 72
    white_dry_time = 50
    dark_wash_time = 58
    dark_dry_time = 65
    color_wash_time = 45
    color_dry_time = 54

    total_time = white_wash_time + white_dry_time + dark_wash_time + dark_dry_time + color_wash_time + color_dry_time
    result = total_time
    return result

print(solution())