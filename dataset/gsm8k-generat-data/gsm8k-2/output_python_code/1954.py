def solution():
    """Ned opens a left-handed store. He sells left-handed mice. They cost 30% more than normal mice. He sells 25 a day and his store is open every day except Sunday, Thursday, and Friday. If normal mice cost $120 how much money does he make a week?"""
    normal_mouse_cost = 120
    left_handed_mouse_cost = normal_mouse_cost * 1.3
    num_left_handed_mice = 25
    num_days_open = 7 - 3  # Store is closed on Sunday, Thursday, and Friday
    total_mice_sold = num_left_handed_mice * num_days_open
    total_sales = total_mice_sold * left_handed_mouse_cost
    result = total_sales
    return result

print(solution())