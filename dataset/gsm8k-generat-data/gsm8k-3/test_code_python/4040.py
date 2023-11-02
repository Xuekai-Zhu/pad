def solution():
    """In Everlee's family, there are two adults and four children. In a cookie jar, there are a total of 120 cookies. If the adults eat 1/3 of the cookies and then gives the rest to the children to divide equally, how many cookies does each child get?"""
    # Define the number of adults and children and the total number of cookies
    num_adults = 2
    num_children = 4
    total_cookies = 120

    # Calculate the number of cookies the adults eat
    adult_cookies = total_cookies // 3

    # Calculate the number of cookies left for the children
    children_cookies = total_cookies - adult_cookies

    # Calculate the number of cookies each child gets
    cookies_per_child = children_cookies // num_children

    # Display the number of cookies each child gets
    result = cookies_per_child
    return result

print(solution())