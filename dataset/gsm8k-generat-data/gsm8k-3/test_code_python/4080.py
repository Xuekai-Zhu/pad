def solution():
    """Karen bakes 50 chocolate chip cookies. She keeps 10 for herself, and she gives 8 to her grandparents. If Karen wants to give everyone in her class cookies, and there are 16 people in her class, how many cookies will each person receive?"""
    # Define the total number of cookies Karen bakes
    TOTAL_COOKIES = 50

    # Define the number of cookies Karen keeps and gives away
    KEPT_COOKIES = 10
    GIVEN_COOKIES = 8

    # Calculate the number of cookies Karen has left to give to her class
    cookies_left = TOTAL_COOKIES - KEPT_COOKIES - GIVEN_COOKIES

    # Calculate the number of cookies each person in Karen's class will receive
    cookies_per_person = cookies_left // 16

    # Display the number of cookies each person will receive
    result = cookies_per_person
    return result

print(solution())