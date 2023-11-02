def solution():
    """Katrina has 120 cookies to sell at her bakery. She plans to take home any cookies she doesn’t sell by the end of the day. In the morning, she sells 3 dozen cookies. During the lunch rush, she sells 57 cookies. In the afternoon, she sells 16 more cookies. How many cookies does she have left to take home?"""
    # Define the total number of cookies
    total_cookies = 120

    # Calculate the number of cookies sold during the morning rush
    morning_cookies = 3 * 12

    # Calculate the total number of cookies sold
    total_sold = morning_cookies + 57 + 16

    # Calculate the number of cookies left to take home
    cookies_left = total_cookies - total_sold

    # Display the number of cookies left to take home
    result = cookies_left
    return result

print(solution())