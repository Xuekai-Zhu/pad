def solution():
    ratio = 4 + 9  # The ratio of Oreos to cookies is 4:9
    total_items = 65  # There are a total of 65 items in the box

    # Calculate the number of Oreos and cookies in the box
    num_oreos = (4 / ratio) * total_items
    num_cookies = (9 / ratio) * total_items

    # Calculate the total cost of buying the Oreos and cookies
    cost_oreos = num_oreos * 2  # Oreos cost $2 each
    cost_cookies = num_cookies * 3  # Cookies cost $3 each

    # Calculate the difference in cost between the cookies and Oreos
    cost_difference = cost_cookies - cost_oreos
    result = cost_difference
    return result

print(solution())