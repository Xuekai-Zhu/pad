def solution():
    """From March to August, Sam made $460 doing 23 hours of yard work. However, from September to February, Sam was only able to work for 8 hours. If Sam is saving up to buy a video game console that costs $600 and has already spent $340 to fix his car, how many more hours does he need to work before he can buy the video game console?"""
    earnings_per_hour = 460 / 23
    total_earnings = earnings_per_hour * (23 + 8)
    total_savings = total_earnings - 340
    remaining_cost = 600 - total_savings
    hours_needed = remaining_cost / earnings_per_hour
    result = hours_needed
    return result

print(solution())