def solution():
    """Katrina has 120 cookies to sell at her bakery. She plans to take home any cookies she doesn’t sell by the end of the day. In the morning, she sells 3 dozen cookies. During the lunch rush, she sells 57 cookies. In the afternoon, she sells 16 more cookies. How many cookies does she have left to take home?"""
    # Define the total number of cookies
    total_cookies = 120

    # Calculate the number of cookies sold in the morning (1 dozen = 12 cookies)
    morning_cookies = 3 * 12

    # Calculate the number of cookies sold during lunch
    lunch_cookies = 57

    # Calculate the number of cookies sold in the afternoon
    afternoon_cookies = 16

    # Calculate the total number of cookies sold
    sold_cookies = morning_cookies + lunch_cookies + afternoon_cookies

    # Calculate the number of cookies left to take home
    remaining_cookies = total_cookies - sold_cookies

    # Return the result
    result = remaining_cookies
    return result

print(solution())