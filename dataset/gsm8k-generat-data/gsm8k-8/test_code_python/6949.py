def solution():
    # Define the calories in one chip
    calories_per_chip = 60/10

    # Calculate the calories in one cheezit (1/3 more than a chip)
    calories_per_cheezit = calories_per_chip * (1 + 1/3)

    # Calculate the total calories from the chips
    chip_calories = 10 * calories_per_chip

    # Calculate the total calories from the cheezits
    cheezit_calories = 6 * calories_per_cheezit

    # Calculate the total calories John ate
    total_calories = chip_calories + cheezit_calories
    result = total_calories
    return result

print(solution())