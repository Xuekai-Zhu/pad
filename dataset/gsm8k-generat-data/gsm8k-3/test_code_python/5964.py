def solution():
    """Betty & Paige are raising money for their kids' little league team by hosting a bake sale.  Betty has baked 4 dozen chocolate chip cookies, 6 dozen oatmeal raisin cookies and 2 dozen regular brownies.  Paige baked 6 dozen sugar cookies, 3 dozen blondies and 5 dozen cream cheese swirled brownies.  If they sell the cookies for $1.00 apiece and the blondies/brownies at $2.00 apiece, how much money will they raise?"""
    
    # Define the prices of cookies and blondies/brownies
    COOKIE_PRICE = 1
    BLONDIE_BROWNIE_PRICE = 2

    # Define the number of dozens of each type of pastry baked
    betty_cookies = 4
    betty_oatmeal_raisin_cookies = 6
    betty_brownies = 2
    paige_sugar_cookies = 6
    paige_blondies = 3
    paige_cream_cheese_swirled_brownies = 5

    # Calculate the total number of each type of pastry baked
    betty_total_cookies = betty_cookies * 12
    betty_total_oatmeal_raisin_cookies = betty_oatmeal_raisin_cookies * 12
    betty_total_brownies = betty_brownies * 12
    paige_total_sugar_cookies = paige_sugar_cookies * 12
    paige_total_blondies = paige_blondies * 12
    paige_total_cream_cheese_swirled_brownies = paige_cream_cheese_swirled_brownies * 12

    # Calculate the total revenue from selling cookies
    total_cookies_revenue = (betty_total_cookies + betty_total_oatmeal_raisin_cookies + betty_total_brownies + 
                            paige_total_sugar_cookies) * COOKIE_PRICE

    # Calculate the total revenue from selling blondies/brownies
    total_blondies_brownies_revenue = (paige_total_blondies + paige_total_cream_cheese_swirled_brownies + 
                                       betty_total_brownies + paige_total_blondies) * BLONDIE_BROWNIE_PRICE

    # Calculate the total revenue from the bake sale
    total_revenue = total_cookies_revenue + total_blondies_brownies_revenue

    # Return the total revenue
    result = total_revenue
    return result

print(solution())