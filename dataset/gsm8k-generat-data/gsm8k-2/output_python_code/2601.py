def solution():
    """Marissa is serving her kids lunch. Each kid gets a burger with 400 calories and 5 carrot sticks with 20 calories each, and some cookies with 50 calories each. Marissa wants each kid to eat a total of 750 calories for lunch. How many cookies does each kid get?"""
    total_calories = 750
    burger_calories = 400
    carrot_calories = 5 * 20
    remaining_calories = total_calories - burger_calories - carrot_calories
    cookies_calories = 50
    cookies_per_kid = remaining_calories // cookies_calories
    result = cookies_per_kid
    return result

print(solution())