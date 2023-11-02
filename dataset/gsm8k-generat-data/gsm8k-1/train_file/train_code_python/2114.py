def solution():
    """For his birthday, Aku invited 4 friends. His mother bought 3 packages of cookies each containing 25 cookies. After playing football, the children came to eat and celebrate Aku's 10th birthday, each eating an equal number of all the cookies. Calculate the number of cookies that each child will eat."""
    num_friends = 4
    num_cookie_packages = 3
    cookies_per_package = 25
    total_cookies = num_cookie_packages * cookies_per_package
    cookies_per_child = total_cookies / (num_friends + 1)
    result = cookies_per_child
    return result

print(solution())