def solution():
    """Samwell owns an appliances store. For this week, one-fourth of their sales are smart TVs, one-eighth are analog TVs,
    and the rest are OLED TVs. If they were able to sell a total of 40 TVs, how many OLED TVs were they able to sell?"""
    total_sales = 40
    smart_tv_sales = total_sales * (1/4)
    analog_tv_sales = total_sales * (1/8)
    oled_tv_sales = total_sales - smart_tv_sales - analog_tv_sales
    result = oled_tv_sales
    return result

print(solution())