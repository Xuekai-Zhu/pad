def solution():
    carrot_calories_per_pound = 51
    broccoli_calories_per_pound = 1/3 * carrot_calories_per_pound
    carrot_amount = 1
    broccoli_amount = 2 * carrot_amount

    # Calculate the total calories from carrots
    total_carrot_calories = carrot_calories_per_pound * carrot_amount

    # Calculate the total calories from broccoli
    total_broccoli_calories = broccoli_calories_per_pound * broccoli_amount

    # Calculate the total calories from both vegetables
    total_calories = total_carrot_calories + total_broccoli_calories
    result = total_calories
    return result

print(solution())