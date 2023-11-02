def solution():
    
    cookies_per_bag = 20
    bags_per_box = 4
    calories_per_cookie = 20
    cookies_per_box = cookies_per_bag * bags_per_box
    calories_per_box = cookies_per_box * calories_per_cookie
    result = calories_per_box
    return result

print(solution())