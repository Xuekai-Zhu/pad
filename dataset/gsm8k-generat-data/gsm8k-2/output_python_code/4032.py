def solution():
    """Tom decided to send his wife 2 dozen roses every day for the week. How many total roses did he send?"""
    roses_per_dozen = 12
    roses_per_day = 2 * roses_per_dozen
    days_in_week = 7
    total_roses = roses_per_day * days_in_week
    result = total_roses
    return result

print(solution())