def solution():
    
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