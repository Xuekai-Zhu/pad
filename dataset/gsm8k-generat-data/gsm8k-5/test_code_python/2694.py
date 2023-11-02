def solution():
    # Calculate Mike's number of cookies
    mike_cookies = 3 * 4  # Millie has 4 cookies, so Mike has 3 times as many

    # Calculate Frank's number of cookies
    frank_cookies = (mike_cookies / 2) - 3  # Frank has three less than half the number of cookies as Mike

    result = frank_cookies
    return result

print(solution())