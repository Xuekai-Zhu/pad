def solution():
    vitamin_a_per_pill = 50  # Each pill has 50 mg of Vitamin A
    daily_serving = 200  # The recommended daily serving of Vitamin A is 200 mg 
    pills_per_day = daily_serving / vitamin_a_per_pill  # Calculate the number of pills needed per day
    pills_per_week = pills_per_day * 7  # Calculate the number of pills needed per week
    result = pills_per_week
    return result

print(solution())