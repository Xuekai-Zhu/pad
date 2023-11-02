def solution():
    box_capacity = 40  # in pounds
    cookie_weight = 0.125  # in pounds (2 ounces = 0.125 pounds)

    # Calculate the total weight of cookies that can fit in the box
    total_cookie_weight = box_capacity

    # Calculate the total number of cookies that can fit in the box
    num_cookies = total_cookie_weight / cookie_weight
    result = int(num_cookies)  # round down to nearest integer
    return result

print(solution())