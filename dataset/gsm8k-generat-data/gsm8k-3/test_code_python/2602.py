def solution():
    """Marissa is serving her kids lunch. Each kid gets a burger with 400 calories and 5 carrot sticks with 20 calories each, and some cookies with 50 calories each. Marissa wants each kid to eat a total of 750 calories for lunch. How many cookies does each kid get?"""
    # Define the number of calories in each item
    BURGER_CALORIES = 400
    CARROT_CALORIES = 20
    COOKIE_CALORIES = 50

    # Define the target number of total calories for each kid
    TARGET_CALORIES = 750

    # Calculate the total number of calories from the burger and carrot sticks
    burger_cal = BURGER_CALORIES
    carrot_cal = 5 * CARROT_CALORIES
    total_cal = burger_cal + carrot_cal

    # Calculate the number of cookies needed to reach the target calories
    cookie_cal = TARGET_CALORIES - total_cal
    num_cookies = cookie_cal // COOKIE_CALORIES

    # Display the number of cookies each kid gets
    result = num_cookies
    return result

print(solution())