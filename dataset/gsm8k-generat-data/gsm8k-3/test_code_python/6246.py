def solution():
    """There were 600 cookies in a box. Nicole ate 2/5 of the total number of cookies, while Eduardo ate 3/5 of the remaining amount. What percentage of the original cookies remained?"""
    # Define the number of cookies in the box
    total_cookies = 600

    # Calculate the number of cookies Nicole ate
    nicole_cookies = int(2/5 * total_cookies)

    # Calculate the number of cookies remaining after Nicole ate
    remaining_cookies = total_cookies - nicole_cookies

    # Calculate the number of cookies Eduardo ate
    eduardo_cookies = int(3/5 * remaining_cookies)

    # Calculate the number of cookies remaining after Eduardo ate
    final_cookies = remaining_cookies - eduardo_cookies

    # Calculate the percentage of cookies remaining compared to the original amount
    percentage_remaining = (final_cookies/total_cookies) * 100

    # Display the percentage of cookies remaining
    result = percentage_remaining
    return result

print(solution())