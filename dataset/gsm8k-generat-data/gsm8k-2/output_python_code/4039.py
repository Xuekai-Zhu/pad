def solution():
    """In Everlee's family, there are two adults and four children. In a cookie jar, there are a total of 120 cookies. If the adults eat 1/3 of the cookies and then gives the rest to the children to divide equally, how many cookies does each child get?"""
    total_cookies = 120
    num_adults = 2
    num_children = 4
    adult_cookies = total_cookies // 3
    child_cookies = total_cookies - adult_cookies
    cookies_per_child = child_cookies // num_children
    result = cookies_per_child
    return result

print(solution())