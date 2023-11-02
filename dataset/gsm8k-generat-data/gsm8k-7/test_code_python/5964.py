def solution():
    # Calculate the total number of each type of baked good
    betty_cookies = 4 * 12
    betty_brownies = 2 * 12
    betty_total = betty_cookies + betty_brownies

    paige_cookies = 6 * 12
    paige_blondies = 3 * 12
    paige_brownies = 5 * 12
    paige_total = paige_cookies + paige_blondies + paige_brownies

    # Calculate the total amount of money raised
    total_money = (betty_cookies + paige_cookies) + (betty_brownies + paige_blondies) * 2 + paige_brownies * 2.5
    result = total_money
    return result

print(solution())