def solution():
    maria_cookies = 19  # Maria has 19 cookies
    friend_cookies = 5  # Maria gave 5 cookies to her friend
    family_cookies = (maria_cookies - friend_cookies) / 2  # Maria gave half of the rest to her family
    maria_cookies -= (friend_cookies + family_cookies)  # Maria gave some cookies, now she has fewer
    maria_cookies -= 2  # Maria decided to eat 2 cookies
    result = maria_cookies  # Final answer is the number of cookies Maria has left
    return result

print(solution())