def solution():
    # Calculate the number of cookies eaten by the adults
    cookies_adults = 120 * (1/3)  # One-third of the cookies are eaten by the adults

    # Calculate the number of cookies left for the children
    cookies_children = 120 - cookies_adults

    # Calculate the number of cookies each child gets
    cookies_per_child = cookies_children / 4  # There are four children in Everlee's family

    result = cookies_per_child
    return result

print(solution())