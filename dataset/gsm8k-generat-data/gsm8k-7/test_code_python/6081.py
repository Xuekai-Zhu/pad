def solution():
    sold_cookies = 50
    earned = 60
    markup = 0.2  # 20% markup

    # Calculate the selling price of each cookie
    price_per_cookie = earned / sold_cookies

    # Calculate the cost to make each cookie
    cost_per_cookie = price_per_cookie / (1 + markup)

    result = cost_per_cookie
    return result

print(solution())