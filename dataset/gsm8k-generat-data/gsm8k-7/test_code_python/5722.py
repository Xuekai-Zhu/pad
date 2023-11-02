def solution():
    num_cookies_mona = 20
    num_cookies_jasmine = num_cookies_mona - 5
    num_cookies_rachel = num_cookies_jasmine + 10

    # Calculate the total number of cookies brought by all three students
    total_cookies = num_cookies_mona + num_cookies_jasmine + num_cookies_rachel
    result = total_cookies
    return result

print(solution())