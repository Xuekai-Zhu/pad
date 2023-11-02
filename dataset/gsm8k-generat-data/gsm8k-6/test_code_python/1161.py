def solution():
    total_cookies = 5*12  # 5 dozen cookies
    sold_cookies = 2*12 + 7 + 2*7  # Mr. Stone buys 2 dozen, Brock buys 7, and Katy buys twice as many as Brock
    remaining_cookies = total_cookies - sold_cookies
    result = remaining_cookies
    return result

print(solution())