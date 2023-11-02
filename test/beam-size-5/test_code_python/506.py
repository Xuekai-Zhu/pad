def solution():
    # Calculate the total calories needed to reach the goal
    total_calories_needed = 30 * 31 + 3500  # 30 lbs for July 19th, 31st is December 31st, and Andy needs to burn 3500 calories to burn a pound

    # Calculate the amount of calorie deficit needed to reach the goal
    calorie_deficit_needed = total_calories_needed / 3500  # Andy needs to burn 3500 calories to burn a pound

    result = calorie_deficit_needed
    return result

print(solution())