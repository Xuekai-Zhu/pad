def solution():
    # Define the number of adults and children
    num_adults = 2
    num_children = 4

    # Calculate the total number of cookies eaten by the adults
    total_cookies_eaten = 120 * (1/3)

    # Calculate the total number of cookies left for the children
    total_cookies_left = 120 - total_cookies_eaten

    # Calculate the number of cookies each child gets
    cookies_per_child = total_cookies_left / num_children
    result = cookies_per_child
    return result

print(solution())