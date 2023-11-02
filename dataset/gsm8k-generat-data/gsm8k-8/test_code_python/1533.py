def solution():
    # Define the variables
    bag_of_cookies = 0
    remaining_cookies = bag_of_cookies - (3/4)*bag_of_cookies
    remaining_cookies = remaining_cookies - (1/2)*remaining_cookies
    remaining_cookies = 8

    # Solve for bag_of_cookies
    bag_of_cookies = remaining_cookies / (1/2)
    result = bag_of_cookies

    return result

print(solution())