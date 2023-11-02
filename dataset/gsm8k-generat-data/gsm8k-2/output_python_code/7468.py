def solution():
    """Josh is saving up for a box of cookies. To raise the money, he is going to make bracelets and sell them. It costs $1 for supplies for each bracelet and he sells each one for $1.5. If he makes 12 bracelets and after buying the cookies still has $3, how much did the box of cookies cost?"""
    total_cost_bracelets = 12 * 1  # each bracelet costs $1 to make
    total_revenue_bracelets = 12 * 1.5  # each bracelet sells for $1.5
    money_left_over = 3  # after buying the box of cookies
    total_money_raised = total_revenue_bracelets - total_cost_bracelets + money_left_over
    cookies_cost = total_money_raised - 12  # subtract money Josh raised from selling bracelets
    result = cookies_cost
    return result

print(solution())