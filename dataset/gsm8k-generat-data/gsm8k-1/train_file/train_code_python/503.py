def solution():
    """From March to August, Sam made $460 doing 23 hours of yard work.
    However, from September to February, Sam was only able to work for 8 hours.
    If Sam is saving up to buy a video game console that costs $600 and has already spent $340 to fix his car,
    how many more hours does he need to work before he can buy the video game console?"""
    total_hours_worked = 23 + 8
    total_money_made = 460
    money_needed = 600 - 340 # cost of video game console - cost of fixing car
    money_per_hour = total_money_made / total_hours_worked
    hours_needed = money_needed / money_per_hour
    result = hours_needed
    return result

print(solution())