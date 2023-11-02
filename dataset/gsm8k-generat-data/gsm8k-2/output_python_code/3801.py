def solution():
    """Claire won a $100 gift card to her favorite coffee shop. She wants to treat herself to a latte that cost $3.75 and a croissant for $3.50 every morning for a week. She also plans to buy 5 cookies that cost $1.25 each. How much money will be left on her card after a week of coffee and pastry?"""
    latte_cost = 3.75
    croissant_cost = 3.5
    cookie_cost = 1.25
    week_total_cost = (latte_cost + croissant_cost) * 7 + cookie_cost * 5
    remaining_balance = 100 - week_total_cost
    result = remaining_balance
    return result

print(solution())