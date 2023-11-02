def solution():
    """In Everlee's family, there are two adults and four children. In a cookie jar, there are a total of 120 cookies. If the adults eat 1/3 of the cookies and then gives the rest to the children to divide equally, how many cookies does each child get?"""
    num_adults = 2
    num_children = 4
    total_cookies = 120
    adult_share = total_cookies / 3
    child_share = (total_cookies - adult_share) / num_children
    result = child_share
    return result

print(solution())