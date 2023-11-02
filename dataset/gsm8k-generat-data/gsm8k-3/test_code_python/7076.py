def solution():
    """The number of Oreos and cookies in a box is in the ratio 4:9. Zane bought each Oreo at $2 and each cookie at $3. How much more money did Zane spend on buying the cookies than buying the Oreos if the total number of items in the box is 65?"""
    # Define the ratio of Oreos to cookies
    OREO_RATIO = 4
    COOKIE_RATIO = 9

    # Define the cost of each Oreo and cookie
    OREO_COST = 2
    COOKIE_COST = 3

    # Define the total number of items in the box
    total_items = 65

    # Calculate the number of Oreos and cookies in the box
    total_ratio = OREO_RATIO + COOKIE_RATIO
    oreos = total_items * (OREO_RATIO / total_ratio)
    cookies = total_items * (COOKIE_RATIO / total_ratio)

    # Calculate the total cost of the Oreos and cookies
    oreo_cost = oreos * OREO_COST
    cookie_cost = cookies * COOKIE_COST

    # Calculate the difference in cost between the cookies and Oreos
    difference = cookie_cost - oreo_cost

    # Display the difference in cost
    result = difference
    return result

print(solution())