def solution():
    """At Peanut Emporium, peanuts cost $3 per pound with a 15-pound minimum. If Baxter spent $105 on peanuts, how many pounds over the minimum did he purchase?"""
    price_per_pound = 3
    minimum_purchase = 15
    total_spent = 105
    pounds_purchased = (total_spent / price_per_pound)
    pounds_over_minimum = pounds_purchased - minimum_purchase
    result = pounds_over_minimum
    return result

print(solution())