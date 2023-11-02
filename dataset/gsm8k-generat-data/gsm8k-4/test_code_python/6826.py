def solution():
    """Lindsay has 4 dolls with blonde hair; four times more dolls with brown than blonde hair; 2 fewer dolls with black than brown hair. How many more dolls with black and brown hair combined does Lindsay have than blonde-haired dolls?"""
    # Define the number of dolls with blonde hair
    blonde_dolls = 4

    # Calculate the number of dolls with brown hair
    brown_dolls = blonde_dolls * 4

    # Calculate the number of dolls with black hair
    black_dolls = brown_dolls - 2

    # Calculate the total number of dolls with black and brown hair
    total_brown_and_black_dolls = brown_dolls + black_dolls

    # Calculate the difference between the total number of black and brown dolls and the number of blonde dolls
    difference = total_brown_and_black_dolls - blonde_dolls

    # return the result
    result = difference
    return result

print(solution())