def solution():
    amazon_share_price = 2500
    netflix_monthly_cost = 8.99
    months_in_twenty_years = 12 * 20
    netflix_cost_over_twenty_years = netflix_monthly_cost * months_in_twenty_years
    if amazon_share_price >= netflix_cost_over_twenty_years:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())