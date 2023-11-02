def solution():
    """Graeme is weighing cookies to see how many he can fit in his box. His box can only hold 40 pounds of cookies. If each cookie weighs 2 ounces, how many cookies can he fit in the box?"""
    # Define the weight limit of the box in ounces
    BOX_WEIGHT_LIMIT = 40 * 16

    # Define the weight of each cookie in ounces
    COOKIE_WEIGHT = 2

    # Calculate the number of cookies that can fit in the box
    max_cookies = BOX_WEIGHT_LIMIT // COOKIE_WEIGHT

    # Return the result
    result = max_cookies
    return result

print(solution())