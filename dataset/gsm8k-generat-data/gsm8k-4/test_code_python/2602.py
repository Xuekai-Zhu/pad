def solution():
    """Marissa is serving her kids lunch. Each kid gets a burger with 400 calories and 5 carrot sticks with 20 calories each, and some cookies with 50 calories each. Marissa wants each kid to eat a total of 750 calories for lunch. How many cookies does each kid get?"""
    # Define the number of calories in a burger, a carrot stick, and a cookie
    BURGER_CALORIES = 400
    CARROT_CALORIES = 20
    COOKIE_CALORIES = 50

    # Define the number of carrot sticks each kid gets
    carrot_sticks = 5

    # Calculate the number of calories from the burger and carrot sticks
    burger_calories = BURGER_CALORIES
    carrot_calories = CARROT_CALORIES * carrot_sticks
    total_calories = burger_calories + carrot_calories

    # Calculate the number of cookies each kid gets to reach the total calorie goal
    cookies = (750 - total_calories) / COOKIE_CALORIES

    result = cookies
    return result

print(solution())