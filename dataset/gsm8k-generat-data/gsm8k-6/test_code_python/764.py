def solution():
    # Calculate the number of calories the dietitian ate
    calories_ate = (3/4) * 40

    # Calculate the number of calories recommended by the FDA
    calories_recommendation = 25

    # Calculate the number of calories above the recommendation that the dietitian ate
    calories_above_recommendation = calories_ate - calories_recommendation

    result = calories_above_recommendation
    return result

print(solution())