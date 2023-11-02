def solution():
    # Calculate the total distance Ian covers in 5 days
    total_distance = 5 * 5 * 100  # 5 laps of 100 feet each, for 5 days

    # Calculate the total number of calories burned
    calories_burned = total_distance / 25  # 25 feet of jogging burns 1 calorie

    result = calories_burned
    return result

print(solution())