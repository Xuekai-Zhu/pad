def solution():
    """For his birthday, Aku invited 4 friends. His mother bought 3 packages of cookies each containing 25 cookies. After playing football, the children came to eat and celebrate Aku's 10th birthday, each eating an equal number of all the cookies. Calculate the number of cookies that each child will eat."""
    total_cookies = 3 * 25
    total_children = 4 + 1 # Aku is also eating
    cookies_per_child = total_cookies // total_children
    result = cookies_per_child
    return result

print(solution())