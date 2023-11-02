def solution():
    cookies_per_bag = 20  # Each bag of cookies has 20 cookies
    bags_per_box = 4  # There are 4 bags in each box
    cookies_per_box = cookies_per_bag * bags_per_box  # Calculate the total number of cookies in a box
    calories_per_cookie = 20  # Each cookie has 20 calories

    # Calculate the total number of calories in a box of cookies
    total_calories = cookies_per_box * calories_per_cookie
    result = total_calories
    return result

print(solution())