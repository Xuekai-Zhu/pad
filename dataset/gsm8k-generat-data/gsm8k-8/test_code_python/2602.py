def solution():
    # Define the calories for each item
    burger_calories = 400
    carrot_calories = 20
    cookie_calories = 50
    
    # Define the total calories for the burger and carrot sticks
    burger_carrot_calories = burger_calories + (5 * carrot_calories)
    
    # Calculate the remaining calories needed for each kid
    remaining_calories = 750 - burger_carrot_calories
    
    # Calculate the number of cookies each kid gets
    cookies_per_kid = remaining_calories / cookie_calories
    result = cookies_per_kid
    return result

print(solution())