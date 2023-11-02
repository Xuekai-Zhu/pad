def solution():
    blonde_hair_dolls = 4  # Lindsay has 4 dolls with blonde hair
    brown_hair_dolls = 4 * 4  # Lindsay has four times more dolls with brown hair than blonde hair
    black_hair_dolls = brown_hair_dolls - 2  # Lindsay has 2 fewer dolls with black hair than brown hair
    total_brown_and_black_dolls = brown_hair_dolls + black_hair_dolls  # Calculate the total number of dolls with brown and black hair
    difference = total_brown_and_black_dolls - blonde_hair_dolls  # Calculate the difference between the total number of dolls with brown and black hair and the number of blonde-haired dolls
    result = difference
    return result

print(solution())