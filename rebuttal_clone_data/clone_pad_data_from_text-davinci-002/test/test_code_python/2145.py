def solution():
    gift_card_amount = 100
    latte_cost = 3.75
    croissant_cost = 3.50
    cookie_cost = 1.25
    pastries_per_day = latte_cost + croissant_cost
    cookies_per_week = cookie_cost * 5
    pastries_per_week = pastries_per_day * 7
    total_cost = pastries_per_week + cookies_per_week
    money_left = gift_card_amount - total_cost
    result = money_left
    return result

print(solution())