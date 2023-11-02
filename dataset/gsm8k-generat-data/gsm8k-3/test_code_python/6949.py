def solution():
    """John eats 10 potato chips that have a total of 60 calories.  He then eats 6 cheezits that each have 1/3 more calories than a chip.  How many total calories did he eat?"""
    
    # Calculate the total calories in the potato chips
    chip_calories = 60
    chip_calories_per_chip = chip_calories / 10

    # Calculate the calories in each cheezit
    cheezit_calories_per_chip = chip_calories_per_chip * 1.333

    # Calculate the total calories in the cheezits
    cheezit_calories = cheezit_calories_per_chip * 6

    # Calculate the total calories John ate
    total_calories = chip_calories + cheezit_calories

    # Display the total calories John ate
    result = total_calories
    return result

print(solution())