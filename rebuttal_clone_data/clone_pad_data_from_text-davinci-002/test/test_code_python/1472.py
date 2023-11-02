def solution():
     calories_per_burger = 400
     calories_per_carrot_stick = 20
     calories_per_cookie = 50
     total_calories = 750
     calories_from_burger_and_carrots = calories_per_burger + (5 * calories_per_carrot_stick)
     calories_from_cookies = total_calories - calories_from_burger_and_carrots
     cookies_per_kid = calories_from_cookies / calories_per_cookie
     result = cookies_per_kid
     return result

print(solution())