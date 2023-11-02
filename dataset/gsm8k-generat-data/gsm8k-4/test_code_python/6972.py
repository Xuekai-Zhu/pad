def solution():
    """A bag of caramel cookies has 20 cookies inside and a box of cookies has 4 bags in total. How many calories are inside the box if each cookie is 20 calories?"""
    # Define the number of cookies per bag and the number of bags per box
    cookies_per_bag = 20
    bags_per_box = 4

    # Calculate the total number of cookies in the box
    total_cookies = cookies_per_bag * bags_per_box

    # Calculate the total number of calories in the box
    calories_per_cookie = 20
    total_calories = total_cookies * calories_per_cookie

    # return the result
    result = total_calories
    return result

print(solution())