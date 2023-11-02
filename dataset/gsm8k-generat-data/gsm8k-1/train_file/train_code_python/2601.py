def solution():
    """Marissa is serving her kids lunch. Each kid gets a burger with 400 calories and 5 carrot sticks with 20 calories each, and some cookies with 50 calories each. Marissa wants each kid to eat a total of 750 calories for lunch. How many cookies does each kid get?"""
    burger_calories = 400
    carrot_stick_calories = 20
    total_calories = 750
    total_calories_without_burger = total_calories - burger_calories
    total_calories_without_carrots = total_calories_without_burger - 5 * carrot_stick_calories
    cookies_calories = 50
    cookies_per_kid = total_calories_without_carrots // cookies_calories
    result = cookies_per_kid
    return result

print(solution())