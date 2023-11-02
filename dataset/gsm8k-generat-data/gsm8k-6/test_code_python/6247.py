def solution():
    # Calculate the total weight of cookies Graeme can fit in the box
    max_weight = 40 * 16  # convert 40 pounds to ounces
    # Find the number of cookies he can fit in the box
    num_cookies = max_weight // 2  # each cookie weighs 2 ounces
    result = num_cookies
    return result

print(solution())