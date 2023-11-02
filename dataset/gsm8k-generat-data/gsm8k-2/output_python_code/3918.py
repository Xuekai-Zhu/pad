def solution():
    """Leila eats cake almost every week. Last week, she ate 6 cakes on Monday, 9 cakes on Friday, and on Saturday, she ate triple the number of cakes she ate on Monday. How many cakes does Leila eat?"""
    monday_cakes = 6
    friday_cakes = 9
    saturday_cakes = 3 * monday_cakes
    total_cakes = monday_cakes + friday_cakes + saturday_cakes
    result = total_cakes
    return result

print(solution())