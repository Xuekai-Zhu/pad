def solution():
    largest_kidney_stone_diameter = 13.0
    quarter_diameter = 2.4
    # Convert kidney stone diameter from cm to mm for easier comparison
    kidney_stone_mm = largest_kidney_stone_diameter * 10
    if kidney_stone_mm > quarter_diameter:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())