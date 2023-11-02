def solution():
    """Andre catches 8 ladybugs on Monday and 5 ladybugs on Tuesday. If each ladybug has 6 dots, how many dots are there in total for all the ladybugs?"""
    # Define the number of ladybugs caught on Monday and Tuesday
    monday_ladybugs = 8
    tuesday_ladybugs = 5

    # Calculate the total number of ladybugs caught
    total_ladybugs = monday_ladybugs + tuesday_ladybugs

    # Calculate the total number of dots in all the ladybugs
    total_dots = total_ladybugs * 6

    # return the result
    result = total_dots
    return result

print(solution())