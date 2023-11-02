def solution():
    blonde_dolls = 4  # number of dolls with blonde hair
    brown_dolls = 4 * 4  # four times more dolls with brown than blonde hair
    black_dolls = brown_dolls - 2  # 2 fewer dolls with black than brown hair
    combined_brown_black = brown_dolls + black_dolls  # number of dolls with brown and black hair combined
    difference = combined_brown_black - blonde_dolls  # difference between the number of dolls with brown and black hair combined and blonde-haired dolls
    result = difference
    return result

print(solution())