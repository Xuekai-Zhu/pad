def solution():
    # Calculate the total number of cookies
    total_cookies = 3 * 25

    # Calculate the number of children
    num_children = 4

    # Calculate the number of cookies each child will eat
    cookies_per_child = total_cookies // num_children
    result = cookies_per_child
    return result

print(solution())