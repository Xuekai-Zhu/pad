def solution():
    """Monica made cookies for herself and her family. Her father ate 10 cookies and her mother ate half as much as the father. Her brother ate 2 more than her mother. How many cookies are left for Monica if she made 30 cookies in total?"""
    # Define the number of cookies eaten by each family member
    father_cookies = 10
    mother_cookies = father_cookies / 2
    brother_cookies = mother_cookies + 2

    # Calculate the total number of cookies eaten
    total_cookies_eaten = father_cookies + mother_cookies + brother_cookies

    # Calculate the number of cookies left for Monica
    monica_cookies = 30 - total_cookies_eaten

    # Display the number of cookies left for Monica
    result = monica_cookies
    return result

print(solution())