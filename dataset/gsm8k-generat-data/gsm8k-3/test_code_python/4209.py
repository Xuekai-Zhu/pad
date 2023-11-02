def solution():
    """Valerie’s cookie recipe makes 16 dozen cookies and calls for 4 pounds of butter.  She only wants to make 4 dozen cookies for the weekend.  How many pounds of butter will she need?"""
    # Define the amount of cookies in one dozen
    COOKIES_PER_DOZEN = 12

    # Define the amount of cookies Valerie wants to make
    cookies_wanted = 4 * COOKIES_PER_DOZEN

    # Calculate the amount of butter needed for 16 dozen cookies
    butter_for_16_dozen = 4

    # Calculate the amount of butter needed for 1 dozen cookies
    butter_for_1_dozen = butter_for_16_dozen / 16

    # Calculate the amount of butter needed for the desired amount of cookies
    butter_for_desired_cookies = butter_for_1_dozen * (cookies_wanted / COOKIES_PER_DOZEN)

    # Display the amount of butter needed
    result = butter_for_desired_cookies
    return result

print(solution())