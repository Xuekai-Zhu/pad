def solution():
    """Lindsay has 4 dolls with blonde hair; four times more dolls with brown than blonde hair; 2 fewer dolls with black than brown hair. How many more dolls with black and brown hair combined does Lindsay have than blonde-haired dolls?"""
    # Define the number of dolls with blonde hair
    BLONDE_DOLLS = 4
    
    # Calculate the number of dolls with brown hair
    BROWN_DOLLS = BLONDE_DOLLS * 4
    
    # Calculate the number of dolls with black hair
    BLACK_DOLLS = BROWN_DOLLS - 2
    
    # Calculate the total number of dolls with brown and black hair combined
    BROWN_AND_BLACK_DOLLS = BROWN_DOLLS + BLACK_DOLLS
    
    # Calculate the difference between the number of brown and black haired dolls and the number of blonde haired dolls
    DIFFERENCE = BROWN_AND_BLACK_DOLLS - BLONDE_DOLLS
    
    # Display the difference
    result = DIFFERENCE
    return result

print(solution())