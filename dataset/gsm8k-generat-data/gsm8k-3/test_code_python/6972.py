def solution():
    """A bag of caramel cookies has 20 cookies inside and a box of cookies has 4 bags in total. How many calories are inside the box if each cookie is 20 calories?"""
    # Define the number of cookies per bag
    COOKIES_PER_BAG = 20

    # Define the number of bags per box
    BAGS_PER_BOX = 4

    # Define the number of calories per cookie
    CALORIES_PER_COOKIE = 20

    # Calculate the total number of cookies in the box
    total_cookies = COOKIES_PER_BAG * BAGS_PER_BOX

    # Calculate the total number of calories in the box
    total_calories = total_cookies * CALORIES_PER_COOKIE

    # Display the total number of calories
    result = total_calories
    return result

print(solution())