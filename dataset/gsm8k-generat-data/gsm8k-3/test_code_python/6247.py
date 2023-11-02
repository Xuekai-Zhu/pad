def solution():
    """Graeme is weighing cookies to see how many he can fit in his box. His box can only hold 40 pounds of cookies. If each cookie weighs 2 ounces, how many cookies can he fit in the box?"""
    # Define the weight of each cookie in ounces
    COOKIE_WEIGHT = 2

    # Define the maximum weight the box can hold in ounces
    BOX_CAPACITY = 40 * 16

    # Calculate the maximum number of cookies Graeme can fit in the box
    max_cookies = BOX_CAPACITY // COOKIE_WEIGHT

    # Display the maximum number of cookies
    result = max_cookies
    return result

print(solution())