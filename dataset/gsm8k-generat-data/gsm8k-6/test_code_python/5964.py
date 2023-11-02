def solution():
    # Calculate the total number of cookies and brownies baked by Betty and Paige
    total_cookies = (4 * 12) + (6 * 12) + (6 * 12) + (3 * 12)  # 4 dozen chocolate chip cookies, 6 dozen oatmeal raisin cookies, 6 dozen sugar cookies, 3 dozen blondies
    total_brownies = (2 * 12) + (5 * 12)  # 2 dozen regular brownies, 5 dozen cream cheese swirled brownies

    # Calculate the total amount of money raised
    total_money = (total_cookies * 1) + (total_brownies * 2)  # cookies sold at $1.00 apiece, blondies/brownies sold at $2.00 apiece
    result = total_money
    return result

print(solution())