def solution():
    oatmeal_raisin_cookies = 3 * 12
    sugar_cookies = 2 * 12
    chocolate_chip_cookies = 4 * 12

    given_away_oatmeal_raisin_cookies = 2 * 12
    given_away_sugar_cookies = 1.5 * 12
    given_away_chocolate_chip_cookies = 2.5 * 12

    total_cookies = (oatmeal_raisin_cookies + sugar_cookies + chocolate_chip_cookies) - \
                    (given_away_oatmeal_raisin_cookies + given_away_sugar_cookies + given_away_chocolate_chip_cookies)
    
    result = total_cookies
    return result

print(solution())