def solution():
    oatmeal_raisin = 3 * 12  # Ann bakes three dozen (36) oatmeal raisin cookies
    sugar = 2 * 12  # Ann bakes two dozen (24) sugar cookies
    chocolate_chip = 4 * 12  # Ann bakes four dozen (48) chocolate chip cookies
    
    oatmeal_raisin_given = 2 * 12  # Ann gives away two dozen (24) oatmeal raisin cookies
    sugar_given = 1.5 * 12  # Ann gives away 1.5 dozen (18) sugar cookies
    chocolate_chip_given = 2.5 * 12  # Ann gives away 2.5 dozen (30) chocolate chip cookies
    
    oatmeal_raisin_kept = oatmeal_raisin - oatmeal_raisin_given  # Ann keeps 12 oatmeal raisin cookies
    sugar_kept = sugar - sugar_given  # Ann keeps 6 sugar cookies
    chocolate_chip_kept = chocolate_chip - chocolate_chip_given  # Ann keeps 18 chocolate chip cookies
    
    total_cookies = oatmeal_raisin_kept + sugar_kept + chocolate_chip_kept  # Ann keeps a total of 36 cookies
    result = total_cookies
    return result

print(solution())