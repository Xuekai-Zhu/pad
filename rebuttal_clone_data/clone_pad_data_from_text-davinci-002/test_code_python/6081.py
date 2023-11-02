def solution():
    total_cookies = 50
    total_money = 60
    percent_markup = 20
    cost_per_cookie = (total_money / total_cookies) / (1 + (percent_markup / 100))
    result = cost_per_cookie
    return result

print(solution())