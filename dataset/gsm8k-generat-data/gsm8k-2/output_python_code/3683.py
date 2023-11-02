def solution():
    """Amelia has laundry to do. She has a load of whites that will take 72 minutes in the washing machine and 50 minutes in the dryer. She has a load of darks that will take 58 minutes in the washing machine and 65 minutes in the dryer. She has a load of colors that will take 45 minutes in the washer and 54 minutes in the dryer. If she does one load at a time, how long will it take her to wash and dry all three loads, in minutes?"""
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