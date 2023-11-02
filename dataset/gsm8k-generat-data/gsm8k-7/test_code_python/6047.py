def solution():
    num_cookies = 60
    num_brownies = 32

    num_cookies_eaten = 2
    num_brownies_eaten = 2

    num_cookies_mom = 1
    num_brownies_mom = 2

    price_cookie = 1
    price_brownie = 1.5

    # Calculate the total number of cookies and brownies available for sale
    num_cookies_left = num_cookies - num_cookies_eaten - num_cookies_mom
    num_brownies_left = num_brownies - num_brownies_eaten - num_brownies_mom

    # Calculate the total amount of money Kyle will make from selling all the cookies and brownies
    total_money = (num_cookies_left * price_cookie) + (num_brownies_left * price_brownie)
    result = total_money
    return result

print(solution())