def solution():
    """At Peanut Emporium, peanuts cost $3 per pound with a 15-pound minimum. If Baxter spent $105 on peanuts, how many pounds over the minimum did he purchase?"""
    peanut_price = 3
    minimum_pounds = 15
    total_cost = 105
    pounds_over_minimum = (total_cost - (minimum_pounds * peanut_price)) / peanut_price
    result = pounds_over_minimum
    return result

print(solution())