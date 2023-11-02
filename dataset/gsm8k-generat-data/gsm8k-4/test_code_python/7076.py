def solution():
    """The number of Oreos and cookies in a box is in the ratio 4:9. Zane bought each Oreo at $2 and each cookie at $3. How much more money did Zane spend on buying the cookies than buying the Oreos if the total number of items in the box is 65?"""
    # Define the ratio of Oreos to cookies
    oreos_ratio = 4
    cookies_ratio = 9

    # Calculate the total number of items in the box
    total_items = 65

    # Calculate the number of Oreos and cookies in the box
    oreos = total_items * (oreos_ratio / (oreos_ratio + cookies_ratio))
    cookies = total_items - oreos

    # Calculate the total amount spent on Oreos and cookies
    oreos_cost = oreos * 2
    cookies_cost = cookies * 3

    # Calculate the difference in cost between cookies and Oreos
    difference = cookies_cost - oreos_cost

    # return the result
    result = difference
    return result

print(solution())