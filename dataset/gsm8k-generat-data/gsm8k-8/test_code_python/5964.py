def solution():
    # Calculate the total number of cookies and brownies baked by Betty and Paige
    betty_cookies = (4 * 12) + (6 * 12)  # 4 dozen chocolate chip + 6 dozen oatmeal raisin
    betty_brownies = 2 * 12  # 2 dozen regular brownies
    paige_cookies = 6 * 12  # 6 dozen sugar cookies
    paige_blondies = 3 * 12  # 3 dozen blondies
    paige_brownies = 5 * 12  # 5 dozen cream cheese swirled brownies

    # Calculate the total amount of money raised from selling cookies and brownies
    cookie_sales = (betty_cookies + paige_cookies) * 1
    brownie_sales = (betty_brownies + paige_blondies + paige_brownies) * 2

    total_sales = cookie_sales + brownie_sales
    result = total_sales
    return result

print(solution())