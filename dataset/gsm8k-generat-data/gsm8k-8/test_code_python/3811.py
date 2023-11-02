def solution():
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

    total_sales = samoas_total + thin_mints_total + fudge_delights_total + sugar_cookies_total
    result = total_sales
    return result

print(solution())