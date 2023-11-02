def solution():
    # Find the number of Oreos and cookies in the box
    total_items = 65
    ratio = 4 / 9
    num_oreos = total_items / (1 + ratio)
    num_cookies = total_items - num_oreos

    # Calculate the total amount spent by Zane on Oreos and cookies
    oreo_cost = 2
    cookie_cost = 3
    total_spent = num_oreos * oreo_cost + num_cookies * cookie_cost

    # Calculate the difference in money spent on buying cookies vs Oreos
    spent_on_cookies = num_cookies * cookie_cost
    spent_on_oreos = num_oreos * oreo_cost
    diff = spent_on_cookies - spent_on_oreos
    result = diff
    return result

print(solution())