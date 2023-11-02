def solution():
    """There were 600 cookies in a box. Nicole ate 2/5 of the total number of cookies, while Eduardo ate 3/5 of the remaining amount. What percentage of the original cookies remained?"""
    # Define the initial number of cookies
    initial_cookies = 600

    # Calculate the number of cookies Nicole ate
    nicole_cookies = initial_cookies * (2/5)

    # Calculate the number of cookies remaining after Nicole ate
    remaining_cookies = initial_cookies - nicole_cookies

    # Calculate the number of cookies Eduardo ate
    eduardo_cookies = remaining_cookies * (3/5)

    # Calculate the number of cookies remaining
    remaining_cookies -= eduardo_cookies

    # Calculate the percentage of initial cookies remaining
    remaining_percentage = (remaining_cookies / initial_cookies) * 100

    # Return the result
    result = remaining_percentage
    return result

print(solution())