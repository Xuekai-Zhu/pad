def solution():
    # Calculate the total number of cookies sold for each type of box
    type1_cookies = 12 * 50  # 50 boxes of 12 cookies each
    type2_cookies = 20 * 80  # 80 boxes of 20 cookies each
    type3_cookies = 16 * 70  # 70 boxes of 16 cookies each

    # Calculate the total number of cookies sold
    total_cookies = type1_cookies + type2_cookies + type3_cookies
    result = total_cookies
    return result

print(solution())