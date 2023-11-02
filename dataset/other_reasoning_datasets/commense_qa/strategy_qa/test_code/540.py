def solution():
    # Define the nutritional value of Snickers
    snickers_nutrition = "high in fat, sugar, and calories, low in nutritional value"
    # Check if Snickers is helpful for weight loss
    if "helpful" not in snickers_nutrition:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())