def solution():
    """Josh is saving up for a box of cookies. To raise the money, he is going to make bracelets and sell them. It costs $1 for supplies for each bracelet and he sells each one for $1.5. If he makes 12 bracelets and after buying the cookies still has $3, how much did the box of cookies cost?"""
    bracelets_made = 12
    supplies_cost = bracelets_made * 1
    sales_revenue = bracelets_made * 1.5
    total_earnings = sales_revenue - supplies_cost - 3
    box_of_cookies_cost = total_earnings
    result = box_of_cookies_cost
    return result

print(solution())