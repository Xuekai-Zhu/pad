def solution():
    # Define the number of cookies each person ate
    father_cookies = 10
    mother_cookies = father_cookies / 2
    brother_cookies = mother_cookies + 2

    # Calculate the total number of cookies eaten
    total_cookies_eaten = father_cookies + mother_cookies + brother_cookies

    # Calculate the number of cookies left for Monica
    cookies_left = 30 - total_cookies_eaten
    result = cookies_left
    return result

print(solution())