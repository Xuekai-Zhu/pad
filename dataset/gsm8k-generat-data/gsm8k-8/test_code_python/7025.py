def solution():
    # Calculate the total number of calories from dinner
    dinner_calories = 110 + 310 + 215

    # Calculate the total number of calories from breakfast and lunch
    total_calories = 560 + 780

    # Calculate the remaining daily calorie allowance
    remaining_calories = 2500 - total_calories - dinner_calories
    result = remaining_calories
    return result

print(solution())