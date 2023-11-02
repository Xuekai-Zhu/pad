def solution():
    normal_mouse_price = 120  # price of a normal mouse
    left_handed_mouse_price = 1.3 * normal_mouse_price  # price of a left-handed mouse (30% more than a normal mouse)
    mice_sold_per_day = 25  # number of mice sold per day
    days_open_per_week = 7 - 3  # assuming the store is closed on Sunday, Thursday, and Friday
    total_mice_sold_per_week = mice_sold_per_day * days_open_per_week  # total number of mice sold per week
    total_money_made_per_week = total_mice_sold_per_week * left_handed_mouse_price  # total money made per week
    result = total_money_made_per_week
    return result

print(solution())