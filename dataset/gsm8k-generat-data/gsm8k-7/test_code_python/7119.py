def solution():
    mustard_oil_liters = 2
    mustard_oil_price = 13

    penne_pasta_pounds = 3
    penne_pasta_price = 4

    pasta_sauce_pounds = 1
    pasta_sauce_price = 5

    total_cost = (mustard_oil_liters * mustard_oil_price) + (penne_pasta_pounds * penne_pasta_price) + (pasta_sauce_pounds * pasta_sauce_price)

    remaining_money = 50 - total_cost
    result = remaining_money
    return result

print(solution())