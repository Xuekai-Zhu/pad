def solution():
    """Annie likes to eat cookies. She ate 5 cookies on Monday, two times more on Tuesday, and 40% more on Wednesday than on Tuesday. How many cookies did Annie eat during these three days?"""
    # Define the number of cookies Annie ate on Monday
    cookies_monday = 5

    # Calculate the number of cookies Annie ate on Tuesday
    cookies_tuesday = cookies_monday * 2

    # Calculate the number of cookies Annie ate on Wednesday
    cookies_wednesday = cookies_tuesday * 1.4

    # Calculate the total number of cookies Annie ate over the three days
    total_cookies = cookies_monday + cookies_tuesday + cookies_wednesday

    # Display the total number of cookies
    result = total_cookies
    return result

print(solution())