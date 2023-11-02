def solution():
    
    peanut_price = 3
    minimum_pounds = 15
    total_cost = 105
    pounds_over_minimum = (total_cost - (minimum_pounds * peanut_price)) / peanut_price
    result = pounds_over_minimum
    return result

print(solution())