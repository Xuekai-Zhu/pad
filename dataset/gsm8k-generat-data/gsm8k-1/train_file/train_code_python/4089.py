def solution():
    """How much money did you make if you sold 220 chocolate cookies at $1 per cookie and 70 vanilla cookies at $2 per cookie?"""
    chocolate_cookies = 220
    vanilla_cookies = 70
    chocolate_price = 1
    vanilla_price = 2
    chocolate_sales = chocolate_cookies * chocolate_price
    vanilla_sales = vanilla_cookies * vanilla_price
    total_sales = chocolate_sales + vanilla_sales
    result = total_sales
    return result

print(solution())