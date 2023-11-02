def solution():
    """The number of Oreos and cookies in a box is in the ratio 4:9. Zane bought each Oreo at $2 and each cookie at $3. How much more money did Zane spend on buying the cookies than buying the Oreos if the total number of items in the box is 65?"""
    total_items = 65
    oreo_ratio = 4
    cookie_ratio = 9
    
    # Use proportion to find the number of Oreos and cookies in the box
    total_ratio = oreo_ratio + cookie_ratio
    oreos = (oreo_ratio/total_ratio) * total_items
    cookies = (cookie_ratio/total_ratio) * total_items
    
    # Calculate the cost of buying Oreos and cookies separately
    oreo_cost = oreos * 2
    cookie_cost = cookies * 3
    
    # Calculate the difference in spending
    spending_difference = cookie_cost - oreo_cost
    result = spending_difference
    
    return result

print(solution())