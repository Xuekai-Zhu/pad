def solution():
    num_adults = 2
    num_children = 4
    total_cookies = 120
    adult_share = total_cookies / 3

    # Calculate the remaining cookies after the adults eat their share
    remaining_cookies = total_cookies - adult_share

    # Calculate the number of cookies each child gets
    num_cookies_per_child = remaining_cookies / num_children
    result = num_cookies_per_child
    return result

print(solution())