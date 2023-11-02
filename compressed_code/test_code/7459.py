def solution():
    
    num_friends = 4
    num_cookie_packages = 3
    cookies_per_package = 25
    total_cookies = num_cookie_packages * cookies_per_package
    cookies_per_child = total_cookies / (num_friends + 1)
    result = cookies_per_child
    return result

print(solution())