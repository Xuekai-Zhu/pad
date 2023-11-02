def solution():
    num_friends = 4
    num_packages = 3
    cookies_per_package = 25
    total_cookies = num_packages * cookies_per_package

    # Calculate the number of cookies each child will eat
    cookies_per_child = total_cookies // num_friends
    
    result = cookies_per_child
    return result

print(solution())