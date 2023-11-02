def solution():
    """Sonny received 45 boxes of cookies from his friend yesterday. He gave 12 to his brother, 9 to his sister, and he gave 7 to his cousin. How many boxes of cookies were left for him?"""
    total_cookies = 45
    cookies_given_away = 12 + 9 + 7
    cookies_left = total_cookies - cookies_given_away
    result = cookies_left
    return result

print(solution())