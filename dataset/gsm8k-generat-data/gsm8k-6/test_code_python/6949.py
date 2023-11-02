def solution():
    # Calculate the total calories in the potato chips
    potato_chip_calories = 60

    # Calculate the calories in each cheezit
    cheezit_calories = (4/3) * (potato_chip_calories / 10)

    # Calculate the total calories in the cheezits
    cheezit_total_calories = 6 * cheezit_calories

    # Calculate the total calories John ate
    total_calories = potato_chip_calories + cheezit_total_calories
    result = total_calories
    return result

print(solution())