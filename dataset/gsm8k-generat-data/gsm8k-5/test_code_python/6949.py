def solution():
    # Calculate the total calories in the 10 potato chips
    calories_per_chip = 60 / 10  # Each chip has 6 calories
    total_potato_chip_calories = calories_per_chip * 10

    # Calculate the calories in each cheezit
    calories_per_cheezit = calories_per_chip * (1/3 + 1)  # Each cheezit has 8 calories

    # Calculate the total calories in the 6 cheezits
    total_cheezit_calories = calories_per_cheezit * 6

    # Calculate the total calories John ate
    total_calories = total_potato_chip_calories + total_cheezit_calories
    result = total_calories
    return result

print(solution())