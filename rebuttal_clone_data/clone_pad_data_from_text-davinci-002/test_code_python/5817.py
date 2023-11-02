def solution():
    neighborhood_A = 10
    neighborhood_B = 5
    cookies_per_house_A = 2
    cookies_per_house_B = 5
    cookie_price = 2
    total_cookies_ sold_A = neighborhood_A * cookies_per_house_A
    total_cookies_sold_B = neighborhood_B * cookies_per_house_B
    total_revenue_A = total_cookies_sold_A * cookie_price
    total_revenue_B = total_cookies_sold_B * cookie_price
    better_choice = max(total_revenue_A, total_revenue_B)
    result = better_choice
    
    return result

print(solution())