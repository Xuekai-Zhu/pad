def solution():
    # Calculate the calories in a pound of carrots
    carrots_calories_per_pound = 51

    # Calculate the calories in a pound of broccoli
    broccoli_calories_per_pound = carrots_calories_per_pound / 3

    # Calculate the calories in Tom's pound of carrots and broccoli
    carrots_calories = carrots_calories_per_pound
    broccoli_calories = broccoli_calories_per_pound * 2
    total_calories = carrots_calories + broccoli_calories
    result = total_calories
    return result

print(solution())