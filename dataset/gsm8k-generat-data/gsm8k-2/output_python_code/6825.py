def solution():
    """Lindsay has 4 dolls with blonde hair; four times more dolls with brown than blonde hair; 2 fewer dolls with black than brown hair. How many more dolls with black and brown hair combined does Lindsay have than blonde-haired dolls?"""
    blonde_hair_dolls = 4
    brown_hair_dolls = 4 * blonde_hair_dolls
    black_hair_dolls = brown_hair_dolls - 2
    total_non_blonde = brown_hair_dolls + black_hair_dolls
    difference = total_non_blonde - blonde_hair_dolls
    result = difference
    return result

print(solution())