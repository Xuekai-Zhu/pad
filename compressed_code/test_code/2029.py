def solution():
    
    total_calories = 750
    burger_calories = 400
    carrot_calories = 5 * 20
    remaining_calories = total_calories - burger_calories - carrot_calories
    cookies_calories = 50
    cookies_per_kid = remaining_calories // cookies_calories
    result = cookies_per_kid
    return result

print(solution())