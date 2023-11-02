def solution():
    samoas_price = 4
    thin_mints_price = 3.5
    fudge_delights_price = 5
    sugar_cookies_price = 2

    num_samoas_green = 3
    num_thin_mints_green = 2
    num_fudge_delights_yellow = 1
    num_sugar_cookies_brown = 9

    total_samoas_cost = samoas_price * num_samoas_green
    total_thin_mints_cost = thin_mints_price * num_thin_mints_green
    total_fudge_delights_cost = fudge_delights_price * num_fudge_delights_yellow
    total_sugar_cookies_cost = sugar_cookies_price * num_sugar_cookies_brown

    total_earnings = total_samoas_cost + total_thin_mints_cost + total_fudge_delights_cost + total_sugar_cookies_cost
    result = total_earnings
    return result

print(solution())