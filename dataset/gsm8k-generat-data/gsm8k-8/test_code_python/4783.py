def solution():
    # Define the amount of Vitamin A in one pill and the recommended daily serving
    vitamin_a_per_pill = 50
    daily_recommended_vitamin_a = 200

    # Calculate the amount of pills needed per day and per week
    pills_per_day = daily_recommended_vitamin_a / vitamin_a_per_pill
    pills_per_week = pills_per_day * 7

    result = pills_per_week
    return result

print(solution())