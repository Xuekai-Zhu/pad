def solution():
    """It costs $.10 to print one page. Jenny wants to print 7 copies of her 25-page essay. She also wants to buy 7 pens that each cost $1.50. If she pays the store with 2 twenty dollar bills, how much money should she get in change?"""
    page_cost = 0.1
    essay_pages = 25
    essay_copies = 7
    total_page_cost = essay_pages * essay_copies * page_cost
    pen_cost = 1.5
    pen_num = 7
    total_pen_cost = pen_cost * pen_num
    total_cost = total_page_cost + total_pen_cost
    twenty_dollar_bills = 2
    paid = twenty_dollar_bills * 20
    change = paid - total_cost
    result = change
    return result

print(solution())