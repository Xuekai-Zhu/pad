def solution():
    # Convert box weight limit to ounces
    box_limit = 40 * 16

    # Calculate the weight of one cookie in ounces
    cookie_weight = 2 / 16

    # Calculate the number of cookies that can fit in the box
    num_cookies = box_limit // cookie_weight
    result = num_cookies
    return result

print(solution())