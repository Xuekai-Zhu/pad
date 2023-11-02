def solution():
    """Betty & Paige are raising money for their kids' little league team by hosting a bake sale. Betty has baked 4 dozen chocolate chip cookies, 6 dozen oatmeal raisin cookies, and 2 dozen regular brownies. Paige baked 6 dozen sugar cookies, 3 dozen blondies, and 5 dozen cream cheese-swirled brownies. If they sell the cookies for $1.00 apiece and the blondies/brownies at $2.00 apiece, how much money will they raise?"""
    chocolate_chip_cookies = 4 * 12
    oatmeal_raisin_cookies = 6 * 12
    regular_brownies = 2 * 12
    sugar_cookies = 6 * 12
    blondies = 3 * 12
    cream_cheese_brownies = 5 * 12
    total_cookies = chocolate_chip_cookies + oatmeal_raisin_cookies
    total_brownies = regular_brownies + blondies + cream_cheese_brownies
    cookies_money = total_cookies * 1
    brownies_money = total_brownies * 2
    total_money = cookies_money + brownies_money
    result = total_money
    return result

print(solution())