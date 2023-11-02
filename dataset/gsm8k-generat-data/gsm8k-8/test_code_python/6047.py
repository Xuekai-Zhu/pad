def solution():
    # Calculate the number of cookies and brownies remaining after Kyle and his mom eat some
    cookies_left = 60 - 2 - 1
    brownies_left = 32 - 2 - 2

    # Calculate the total amount of money Kyle can make
    cookie_profit = cookies_left * 1
    brownie_profit = brownies_left * 1.5
    total_profit = cookie_profit + brownie_profit

    result = total_profit
    return result

print(solution())