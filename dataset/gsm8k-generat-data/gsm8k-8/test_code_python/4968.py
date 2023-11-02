def solution():
    # Define the weight of carrots and broccoli
    carrot_weight = 1
    broccoli_weight = 2

    # Define the calorie counts per pound
    carrot_calories = 51
    broccoli_calories = carrot_calories / 3

    # Calculate the total calories consumed
    total_calories = (carrot_weight * carrot_calories) + (broccoli_weight * broccoli_calories)
    result = total_calories
    return result

print(solution())