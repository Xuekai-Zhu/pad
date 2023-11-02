def solution():
    total_calories = 40
    recommended_calories = 25

    # Calculate the amount of calories the dietitian ate
    ate_calories = total_calories * 0.75

    # Calculate the amount of calories over the recommended daily intake
    over_intake_calories = ate_calories - recommended_calories
    result = over_intake_calories
    return result

print(solution())