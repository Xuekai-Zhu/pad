def solution():
    # Define the starting number of cookies
    starting_cookies = 600

    # Calculate the number of cookies Nicole ate
    nicole_cookies = starting_cookies * (2/5)
    remaining_cookies = starting_cookies - nicole_cookies

    # Calculate the number of cookies Eduardo ate
    eduardo_cookies = remaining_cookies * (3/5)

    # Calculate the number of cookies remaining
    remaining_cookies = remaining_cookies - eduardo_cookies

    # Calculate the percentage of the original cookies remaining
    percent_remaining = (remaining_cookies / starting_cookies) * 100
    result = percent_remaining
    return result

print(solution())