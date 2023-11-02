def solution():
    # Define the number of cookies per bag and per box
    cookies_per_bag = 20
    bags_per_box = 4

    # Calculate the total number of cookies in the box
    cookies_per_box = cookies_per_bag * bags_per_box

    # Calculate the total number of calories in the box
    calories_per_cookie = 20
    total_calories = cookies_per_box * calories_per_cookie

    result = total_calories
    return result

print(solution())