def solution():
    """Kristy baked cookies because her friends are coming over to her house. She ate 2 of them and gave her brother 1 cookie. Her first friend arrived and took 3 cookies. The second and third friends to arrive took 5 cookies each. If there are 6 cookies left, how many cookies did Kristy bake?"""
    # Calculate the total number of cookies taken by Kristy's friends
    friends_cookies = 3 + 5 + 5
    # Calculate the total number of cookies taken from the original batch
    total_cookies_taken = 2 + 1 + friends_cookies
    # Calculate the total number of cookies Kristy baked
    total_cookies = total_cookies_taken + 6
    result = total_cookies
    return result

print(solution())