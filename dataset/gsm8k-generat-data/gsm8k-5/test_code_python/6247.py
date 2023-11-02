def solution():
    max_weight = 40  # The box can hold a maximum of 40 pounds of cookies
    cookie_weight = 0.125  # 2 ounces is equal to 0.125 pounds
    max_cookies = int(max_weight / cookie_weight)  # Calculate the maximum number of cookies that can fit in the box
    result = max_cookies
    return result

print(solution())