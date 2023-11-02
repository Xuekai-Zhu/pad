def solution():
    """Monica made cookies for herself and her family. Her father ate 10 cookies and her mother ate half as much as the father. Her brother ate 2 more than her mother. How many cookies are left for Monica if she made 30 cookies in total?"""
    # Define the number of cookies Monica made and the number of cookies each family member ate
    total_cookies = 30
    father_cookies = 10
    mother_cookies = father_cookies / 2
    brother_cookies = mother_cookies + 2

    # Calculate the number of cookies remaining for Monica
    remaining_cookies = total_cookies - father_cookies - mother_cookies - brother_cookies

    result = remaining_cookies
    return result

print(solution())