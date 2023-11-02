def solution():
    betty_cookies = 4 + 6 + 2
    betty_blondies = 0
    betty_brownies = 0
    paige_cookies = 6 + 3 + 5
    paige_blondies = 3
    paige_brownies = 5
    total_cookies = betty_cookies + paige_cookies
    total_blondies = betty_blondies + paige_blondies
    total_brownies = betty_brownies + paige_brownies
    cookie_price = 1
    blondie_price = 2
    brownie_price = 2
    total_sale = (total_cookies * cookie_price) + (total_blondies * blondie_price) + (total_brownies * brownie_price)
    result = total_sale
    return result

print(solution())