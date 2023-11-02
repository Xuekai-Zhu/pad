def solution():
    cookies_on_monday = 5
    cookies_on_tuesday = 2 * cookies_on_monday  # Annie ate two times more cookies on Tuesday
    cookies_on_wednesday = 1.4 * cookies_on_tuesday  # Annie ate 40% more cookies on Wednesday than on Tuesday

    # Calculate the total number of cookies Annie ate in three days
    total_cookies = cookies_on_monday + cookies_on_tuesday + cookies_on_wednesday
    result = total_cookies
    return result

print(solution())