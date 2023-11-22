def solution():
    
    packs_of_cookies = 10
    cookies_per_pack = 6
    cost_per_cookie = 0.10
    total_cookies = packs_of_cookies * cookies_per_pack
    total_cost = total_cookies * cost_per_cookie
    payment = 10
    change = payment - total_cost
    result = change
    return result

print(solution())