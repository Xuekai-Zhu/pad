def solution():
    """Neil baked 20 cookies. He gave 2/5 of the cookies to his friend. How many cookies are left for Neil?"""
    # Define the number of cookies baked
    num_cookies_baked = 20

    # Calculate the number of cookies given to Neil's friend
    num_cookies_given_away = int(num_cookies_baked * (2/5))

    # Calculate the number of cookies left for Neil
    num_cookies_left = num_cookies_baked - num_cookies_given_away

    # Display the number of cookies left for Neil
    result = num_cookies_left
    return result

print(solution())