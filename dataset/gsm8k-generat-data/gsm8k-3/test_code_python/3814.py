def solution():
    """Andre catches 8 ladybugs on Monday and 5 ladybugs on Tuesday. If each ladybug has 6 dots, how many dots are there in total for all the ladybugs?"""
    # Define the number of ladybugs caught each day and the number of dots per ladybug
    MONDAY_LADYBUGS = 8
    TUESDAY_LADYBUGS = 5
    DOTS_PER_LADYBUG = 6

    # Calculate the total number of ladybugs caught
    total_ladybugs = MONDAY_LADYBUGS + TUESDAY_LADYBUGS

    # Calculate the total number of dots
    total_dots = total_ladybugs * DOTS_PER_LADYBUG

    # Display the total number of dots
    result = total_dots
    return result

print(solution())