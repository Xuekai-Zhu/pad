def solution():
    """Kristy baked cookies because her friends are coming over to her house. She ate 2 of them and gave her brother 1 cookie. Her first friend arrived and took 3 cookies. The second and third friends to arrive took 5 cookies each. If there are 6 cookies left, how many cookies did Kristy bake?"""
    # Define the initial number of cookies
    initial_cookies = None

    # Define the number of cookies eaten by Kristy and given to her brother
    kristy_cookies = 2 + 1

    # Define the number of cookies taken by the first friend
    friend1_cookies = 3

    # Define the number of cookies taken by the second and third friends
    friend2_cookies = 5
    friend3_cookies = 5

    # Define the number of cookies left
    cookies_left = 6

    # Calculate the total number of cookies baked
    initial_cookies = kristy_cookies + friend1_cookies + friend2_cookies + friend3_cookies + cookies_left

    result = initial_cookies
    return result

print(solution())