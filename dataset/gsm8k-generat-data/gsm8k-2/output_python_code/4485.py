def solution():
    """Annie likes to eat cookies. She ate 5 cookies on Monday, two times more on Tuesday, and 40% more on Wednesday than on Tuesday. How many cookies did Annie eat during these three days?"""
    monday_cookies = 5
    tuesday_cookies = monday_cookies * 2
    wednesday_cookies = tuesday_cookies * 1.4
    total_cookies = monday_cookies + tuesday_cookies + wednesday_cookies
    result = total_cookies
    return result

print(solution())