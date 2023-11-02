def solution():
    # Calculate the total number of cookies
    total_cookies = 3 * 25  # 3 packages of cookies each containing 25 cookies

    # Calculate the number of children
    num_children = 4 + 1  # Aku and his 4 friends

    # Calculate the number of cookies each child will eat
    cookies_per_child = total_cookies // num_children  # integer division
    result = cookies_per_child
    return result

print(solution())