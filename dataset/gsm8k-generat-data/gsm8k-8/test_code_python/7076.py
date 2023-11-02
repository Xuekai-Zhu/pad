def solution():
    # Define the ratio
    oreo_to_cookie_ratio = 4/9

    # Calculate the number of Oreos and cookies in the box
    total_items = 65
    total_ratio = 4 + 9
    oreo_count = (oreo_to_cookie_ratio * total_items) / total_ratio
    cookie_count = total_items - oreo_count

    # Calculate the total cost of buying Oreos and cookies
    oreo_cost = oreo_count * 2
    cookie_cost = cookie_count * 3

    # Calculate the difference in cost between buying cookies and Oreos
    cost_difference = cookie_cost - oreo_cost
    result = cost_difference
    return result

print(solution())