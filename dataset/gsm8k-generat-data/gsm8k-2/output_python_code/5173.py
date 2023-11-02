def solution():
    """Alex needs to be 54 inches tall to ride the newest roller coaster at the theme park. He is 48 inches tall this year. He hears a rumor that for every hour he hangs upside down, he can grow 1/12 of an inch. Normally he grows 1/3 of an inch per month. On average, how many hours does he need to hang upside down each month to be tall enough next year to ride the rollercoaster?"""
    inches_needed = 54
    current_height = 48
    inches_to_grow = inches_needed - current_height
    upside_down_growth_rate = 1/12
    normal_growth_rate = 1/3
    hours_per_month = inches_to_grow / (normal_growth_rate + upside_down_growth_rate)
    result = hours_per_month
    return result

print(solution())