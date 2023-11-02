def solution():
    """Carmen is selling girl scout cookies. She sells three boxes of samoas to the green house for $4 each; two boxes of thin mints for $3.50 each and one box of fudge delights for $5 to the yellow house; and nine boxes of sugar cookies for $2 each to the brown house. How much money did Carmen make?"""
    samoas_price = 4
    thin_mints_price = 3.5
    fudge_delights_price = 5
    sugar_cookies_price = 2

    samoas_sold = 3
    thin_mints_sold = 2
    fudge_delights_sold = 1
    sugar_cookies_sold = 9

    samoas_total = samoas_sold * samoas_price
    thin_mints_total = thin_mints_sold * thin_mints_price
    fudge_delights_total = fudge_delights_sold * fudge_delights_price
    sugar_cookies_total = sugar_cookies_sold * sugar_cookies_price

    total_money = samoas_total + thin_mints_total + fudge_delights_total + sugar_cookies_total
    result = total_money
    return result

print(solution())