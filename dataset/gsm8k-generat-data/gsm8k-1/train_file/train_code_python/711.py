def solution():
    """Jimmy bought 3 pens for school for $1 each, 4 notebooks for $3 each and 2 folders for $5 each. If he paid with a $50 bill, how much change will he get back?"""
    pen_cost = 3 * 1
    notebook_cost = 4 * 3
    folder_cost = 2 * 5
    total_cost = pen_cost + notebook_cost + folder_cost
    payment = 50
    change = payment - total_cost
    result = change
    return result

print(solution())