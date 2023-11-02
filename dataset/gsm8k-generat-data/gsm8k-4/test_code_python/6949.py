def solution():
    """John eats 10 potato chips that have a total of 60 calories. He then eats 6 cheezits that each have 1/3 more calories than a chip. How many total calories did he eat?"""
    # Define the number of potato chips and their total calories
    num_chips = 10
    chip_calories = 60

    # Define the calories per cheezit
    cheezit_calories = chip_calories * 1.33

    # Calculate the total calories from eating cheezits
    total_cheezit_calories = cheezit_calories * 6

    # Calculate the total calories from eating both chips and cheezits
    total_calories = chip_calories + total_cheezit_calories

    # return the result
    result = total_calories
    return result

print(solution())