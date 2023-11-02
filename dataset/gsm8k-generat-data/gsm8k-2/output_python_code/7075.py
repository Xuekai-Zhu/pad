def solution():
    """The number of Oreos and cookies in a box is in the ratio 4:9. Zane bought each Oreo at $2 and each cookie at $3. How much more money did Zane spend on buying the cookies than buying the Oreos if the total number of items in the box is 65?"""
    oreos_ratio = 4
    cookies_ratio = 9
    total_items = 65
    total_ratio = oreos_ratio + cookies_ratio
    oreos_count = (oreos_ratio / total_ratio) * total_items
    cookies_count = (cookies_ratio / total_ratio) * total_items
    oreos_cost = oreos_count * 2
    cookies_cost = cookies_count * 3
    difference = cookies_cost - oreos_cost
    result = difference
    return result

print(solution())