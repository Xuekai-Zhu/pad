def solution():
    cookies_at_start = 3 + 5  # Andy ate 3 cookies and gave 5 to his brother
    players = 8  # There are 8 players in the basketball team

    # Calculate the total number of cookies taken by the players
    total_cookies_taken = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15

    # Calculate the total number of cookies Andy had at the start
    total_cookies = cookies_at_start + total_cookies_taken
    result = total_cookies
    return result

print(solution())