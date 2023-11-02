def solution():
    """There were 600 cookies in a box. Nicole ate 2/5 of the total number of cookies, while Eduardo ate 3/5 of the remaining amount. What percentage of the original cookies remained?"""
    total_cookies = 600
    nicole_cookies = total_cookies * 2/5
    remaining_cookies = total_cookies - nicole_cookies
    eduardo_cookies = remaining_cookies * 3/5
    remaining_percentage = (remaining_cookies - eduardo_cookies) / total_cookies * 100
    result = remaining_percentage
    return result

print(solution())