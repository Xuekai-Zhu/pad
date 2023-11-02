def solution():
    """Ned opens a left-handed store. He sells left-handed mice. They cost 30% more than normal mice. He sells 25 a day and his store is open every day except Sunday, Thursday, and Friday. If normal mice cost $120 how much money does he make a week?"""
    normal_mouse_cost = 120
    left_handed_mouse_cost = normal_mouse_cost * 1.3
    mice_sold_per_day = 25
    days_open_per_week = 7 - 3 - 1 - 1  # 7 days in a week, closed on Sunday, Thursday, and Friday
    total_mice_sold_per_week = mice_sold_per_day * days_open_per_week
    total_money_made_per_week = total_mice_sold_per_week * left_handed_mouse_cost
    result = total_money_made_per_week
    return result

print(solution())