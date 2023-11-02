def solution():
    """Jackie is trying to decide whether to do her taxes herself or hire an accountant. If she does the taxes herself, she'll be able to do 3 fewer hours of freelance work, losing $35/hour in missed income. The accountant charges $90. How much more money will she have if she hires the accountant?"""
    freelance_hours_lost = 3
    hourly_rate = 35
    accountant_cost = 90
    money_saved = freelance_hours_lost * hourly_rate
    money_saved -= accountant_cost
    result = money_saved
    return result

print(solution())