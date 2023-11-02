def solution():
    """May is getting her hair cut and colored. It costs $40 for the color and $30 per inch of
    haircut. If her hair started at 10 inches and ended at 8, how much did her cut and color cost?"""
    color_cost = 40
    start_length = 10
    end_length = 8
    inches_cut = start_length - end_length
    haircut_cost = inches_cut * 30
    total_cost = color_cost + haircut_cost
    result = total_cost
    return result

print(solution())