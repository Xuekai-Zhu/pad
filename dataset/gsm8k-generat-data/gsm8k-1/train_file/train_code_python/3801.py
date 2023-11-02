def solution():
    """Claire won a $100 gift card to her favorite coffee shop. She wants to treat herself to a latte that cost $3.75 and a croissant for $3.50 every morning for a week. She also plans to buy 5 cookies that cost $1.25 each. How much money will be left on her card after a week of coffee and pastry?"""
    gift_card = 100
    latte_cost = 3.75
    croissant_cost = 3.50
    cookie_cost = 1.25
    days_per_week = 7
    
    total_cost_per_day = latte_cost + croissant_cost + (5*cookie_cost)
    total_cost_per_week = total_cost_per_day * days_per_week
    money_left = gift_card - total_cost_per_week
    result = money_left
    
    return result

print(solution())