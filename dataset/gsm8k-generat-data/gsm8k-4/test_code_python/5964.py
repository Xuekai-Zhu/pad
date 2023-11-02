def solution():
    """Betty & Paige are raising money for their kids' little league team by hosting a bake sale.  Betty has baked 4 dozen chocolate chip cookies, 6 dozen oatmeal raisin cookies and 2 dozen regular brownies.  Paige baked 6 dozen sugar cookies, 3 dozen blondies and 5 dozen cream cheese swirled brownies.  If they sell the cookies for $1.00 apiece and the blondies/brownies at $2.00 apiece, how much money will they raise?"""
    # Define the prices of the different items
    cookie_price = 1
    brownie_price = 2
    blondie_price = 2

    # Calculate the total number of items baked by Betty and Paige
    total_cookies = (4 + 6) * 12
    total_brownies = (2 + 5) * 12
    total_blondies = 3 * 12
    total_items = total_cookies + total_brownies + total_blondies

    # Calculate the total amount of money raised
    total_money = (total_cookies * cookie_price) + (total_brownies * brownie_price) + (total_blondies * blondie_price)
    result = total_money
    return result

print(solution())