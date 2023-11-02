def solution():
    """Lindsay has 4 dolls with blonde hair; four times more dolls with brown than blonde hair; 2 fewer dolls with black than brown hair.
    How many more dolls with black and brown hair combined does Lindsay have than blonde-haired dolls?"""
    blonde_dolls = 4
    brown_dolls = blonde_dolls * 4
    black_dolls = brown_dolls - 2
    total_brown_and_black = brown_dolls + black_dolls
    difference = total_brown_and_black - blonde_dolls
    result = difference
    return result

print(solution())