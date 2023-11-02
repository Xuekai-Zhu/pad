def solution():
    oreo_ratio = 4
    cookie_ratio = 9
    oreo_price = 2
    cookie_price = 3
    total_items = 65

    # Calculate the total number of Oreo and cookie items based on the ratio
    total_ratio = oreo_ratio + cookie_ratio
    num_oreos = (oreo_ratio / total_ratio) * total_items
    num_cookies = (cookie_ratio / total_ratio) * total_items

    # Calculate the total amount spent on Oreos
    oreo_cost = num_oreos * oreo_price

    # Calculate the total amount spent on cookies
    cookie_cost = num_cookies * cookie_price

    # Calculate the difference between the amount spent on cookies and Oreos
    difference = cookie_cost - oreo_cost
    result = difference
    return result

print(solution())