def solution():
    """Peggy has 6 dolls. Her grandmother gives Peggy her own collection of 30 dolls. Over the year, Peggy receives half that amount of dolls between her birthday and Christmas. How many dolls does Peggy now have?"""
    # Define the number of dolls Peggy started with and the number her grandmother gave her
    INITIAL_DOLLS = 6
    GRANDMOTHER_DOLLS = 30

    # Calculate how many dolls Peggy received between her birthday and Christmas
    BIRTHDAY_TO_CHRISTMAS_DOLLS = GRANDMOTHER_DOLLS / 2

    # Calculate Peggy's total number of dolls
    total_dolls = INITIAL_DOLLS + GRANDMOTHER_DOLLS + BIRTHDAY_TO_CHRISTMAS_DOLLS

    # Display Peggy's total number of dolls
    result = total_dolls
    return result

print(solution())