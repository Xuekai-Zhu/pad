def solution():
    """Karen bakes 50 chocolate chip cookies. She keeps 10 for herself, and she gives 8 to her grandparents. If Karen wants to give everyone in her class cookies, and there are 16 people in her class, how many cookies will each person receive?"""
    # Define the number of cookies Karen baked
    total_cookies = 50

    # Calculate the number of cookies Karen has left after keeping some for herself and giving some to her grandparents
    remaining_cookies = total_cookies - 10 - 8

    # Calculate the number of cookies each person in her class will receive
    cookies_per_person = remaining_cookies / 16

    # Round the result to the nearest whole number and return it
    result = round(cookies_per_person)
    return result

print(solution())