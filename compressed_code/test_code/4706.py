def solution():
    
    num_cookies = 50
    earnings = 60
    markup_percentage = 20
    markup_factor = 1 + (markup_percentage / 100)
    price_per_cookie = earnings / num_cookies
    cost_per_cookie = price_per_cookie / markup_factor
    result = cost_per_cookie
    return result

print(solution())