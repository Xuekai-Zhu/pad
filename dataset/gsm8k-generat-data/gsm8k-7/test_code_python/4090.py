def solution():
    num_chocolate_cookies = 220
    chocolate_cookie_price = 1.0

    num_vanilla_cookies = 70
    vanilla_cookie_price = 2.0

    # Calculate the total revenue from selling chocolate cookies
    chocolate_cookie_revenue = num_chocolate_cookies * chocolate_cookie_price

    # Calculate the total revenue from selling vanilla cookies
    vanilla_cookie_revenue = num_vanilla_cookies * vanilla_cookie_price

    # Calculate the total revenue from selling all cookies
    total_revenue = chocolate_cookie_revenue + vanilla_cookie_revenue
    result = total_revenue
    return result

print(solution())