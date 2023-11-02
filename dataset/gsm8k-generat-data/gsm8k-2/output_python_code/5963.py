def solution():
    """Betty & Paige are raising money for their kids' little league team by hosting a bake sale. Betty has baked 4 dozen chocolate chip cookies, 6 dozen oatmeal raisin cookies and 2 dozen regular brownies.
    Paige baked 6 dozen sugar cookies, 3 dozen blondies and 5 dozen cream cheese swirled brownies. If they sell the cookies for $1.00 apiece and the blondies/brownies at $2.00 apiece, how much money will they raise?"""
    
    # Calculate the number of items baked by each person
    betty_choc_chip = 4 * 12
    betty_oatmeal = 6 * 12
    betty_brownies = 2 * 12
    paige_sugar = 6 * 12
    paige_blondies = 3 * 12
    paige_cream_cheese = 5 * 12
    
    # Calculate the total amount of money raised
    total_cookies_money = (betty_choc_chip + betty_oatmeal + paige_sugar) * 1
    total_brownies_money = (betty_brownies + paige_blondies + paige_cream_cheese) * 2
    total_money = total_cookies_money + total_brownies_money
    
    result = total_money
    return result

print(solution())