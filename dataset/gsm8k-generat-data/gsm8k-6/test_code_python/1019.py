def solution():
    # Calculate the total number of cookies baked by Alice and Bob
    total_cookies = 74 + 7  # 74 chocolate chip cookies and 7 peanut butter cookies
    # Calculate the total number of cookies baked after the accidents
    total_cookies_after = (74+5) + (7+36)  # 5 more cookies by Alice and 36 more by Bob
    # Calculate the number of cookies thrown on the floor
    cookies_thrown = total_cookies - total_cookies_after + 93  # 93 cookies were left at the end
    result = cookies_thrown
    return result

print(solution())