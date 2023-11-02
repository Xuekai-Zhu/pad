def solution():
    """Annie likes to eat cookies. She ate 5 cookies on Monday, two times more on Tuesday,
    and 40% more on Wednesday than on Tuesday. How many cookies did Annie eat during these three days?"""
    # Define the number of cookies eaten on Monday
    monday_cookies = 5

    # Define the number of cookies eaten on Tuesday
    tuesday_cookies = monday_cookies * 2

    # Define the percentage increase in cookies eaten on Wednesday compared to Tuesday
    wednesday_increase = 0.4

    # Calculate the number of cookies eaten on Wednesday
    wednesday_cookies = tuesday_cookies + (tuesday_cookies * wednesday_increase)

    # Calculate the total number of cookies eaten during the three days
    total_cookies = monday_cookies + tuesday_cookies + wednesday_cookies

    result = total_cookies
    return result

print(solution())