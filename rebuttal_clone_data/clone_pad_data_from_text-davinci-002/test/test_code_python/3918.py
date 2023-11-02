def solution():
    cookies_per_bag = 20
    bags_per_box = 4
    calories_per_cookie = 20
    total_cookies = cookies_per_bag * bags_per_box
    total_calories = total_cookies * calories_per_cookie
    result = total_calories
    return result

print(solution())