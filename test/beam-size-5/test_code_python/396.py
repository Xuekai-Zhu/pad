def solution():
    milk_per_glass = 8  # A glass of milk is 8 ounces of milk
    glasses_drunk = 2  # John drinks 2 glasses of milk
    calories_per_ounce = 3  # Milk has 3 calories per ounce

    # Calculate the total amount of milk consumed
    total_milk = milk_per_glass * glasses_drunk

    # Calculate the total number of calories consumed
    total_calories = total_milk * calories_per_ounce
    result = total_calories
    return result

print(solution())