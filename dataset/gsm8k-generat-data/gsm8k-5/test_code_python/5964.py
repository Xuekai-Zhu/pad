def solution():
    # Calculate the total number of each type of baked goods
    betty_cookies = 4 * 12
    betty_brownies = 2 * 12
    betty_total = betty_cookies + betty_brownies

    paige_cookies = 6 * 12
    paige_blondies = 3 * 12
    paige_brownies = 5 * 12
    paige_total = paige_cookies + paige_blondies + paige_brownies

    # Calculate the total amount of money raised
    total_money = betty_total + paige_total
    total_cookies = betty_cookies + paige_cookies

    # Calculate the amount of money raised from cookies and brownies
    cookie_money = total_cookies * 1.00
    brownie_money = (betty_brownies + paige_brownies + paige_blondies) * 2.00
    total_sales = cookie_money + brownie_money

    result = total_sales
    return result

print(solution())