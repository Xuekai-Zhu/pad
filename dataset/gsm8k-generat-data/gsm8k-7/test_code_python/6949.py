def solution():
    chips_calories = 6  # total calories in 10 potato chips
    chips_count = 10
    cheezit_calories_ratio = 1 + 1/3  # 1/3 more calories than a potato chip
    cheezit_count = 6

    # Calculate the total calories from chips
    total_chips_calories = chips_calories * chips_count

    # Calculate the calories in one cheezit
    cheezit_calories = chips_calories * cheezit_calories_ratio

    # Calculate the total calories from cheezits
    total_cheezit_calories = cheezit_calories * cheezit_count

    # Calculate the total calories consumed
    total_calories = total_chips_calories + total_cheezit_calories
    result = total_calories
    return result

print(solution())