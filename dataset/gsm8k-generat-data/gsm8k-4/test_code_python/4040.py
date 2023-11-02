def solution():
    """In Everlee's family, there are two adults and four children. In a cookie jar, there are a total of 120 cookies. If the adults eat 1/3 of the cookies and then gives the rest to the children to divide equally, how many cookies does each child get?"""
    # Define the number of adults and children in the family
    num_adults = 2
    num_children = 4

    # Define the total number of cookies in the jar
    total_cookies = 120

    # Calculate the number of cookies the adults eat
    num_adult_cookies = total_cookies * (1/3)

    # Calculate the number of cookies remaining for the children
    num_child_cookies = total_cookies - num_adult_cookies

    # Calculate the number of cookies each child gets
    num_cookies_per_child = num_child_cookies / num_children

    # Return the result
    result = num_cookies_per_child
    return result

print(solution())