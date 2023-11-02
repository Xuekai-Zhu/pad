def solution():
    """Susan had a sum of money. She spent 1/5 of it in September, 1/4 of it in October, and $120 in November. After spending these amounts of money, she still had $540 left. How much money did she have at first?"""
    november_spending = 120
    remaining_money = 540
    total_spending = november_spending + remaining_money
    september_spending = total_spending / 5
    october_spending = total_spending / 4
    total_money = total_spending + september_spending + october_spending
    result = total_money
    return result

print(solution())