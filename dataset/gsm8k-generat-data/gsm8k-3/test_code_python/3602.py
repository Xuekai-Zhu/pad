def solution():
    """Jackson's oldest son gets 4 cookies after school and his youngest son gets 2 cookies after school.  If there are 54 cookies in a box, how many days will the box last?"""
    # Define the number of cookies each son gets per day
    OLDEST_SON_COOKIES_PER_DAY = 4
    YOUNGEST_SON_COOKIES_PER_DAY = 2

    # Define the total number of cookies each day
    TOTAL_COOKIES_PER_DAY = OLDEST_SON_COOKIES_PER_DAY + YOUNGEST_SON_COOKIES_PER_DAY

    # Define the number of cookies in a box
    COOKIES_PER_BOX = 54

    # Calculate the number of days the box will last
    days = COOKIES_PER_BOX / TOTAL_COOKIES_PER_DAY

    # Display the number of days
    result = days
    return result

print(solution())