def solution():
    discount = 0.2  # 20% discount on the $300 lens
    price_with_discount = 300 - (discount * 300)  # Calculate the price of the discounted lens
    cheaper_lense_cost = 220  # Cost of the cheaper lens

    # Calculate how much money Mark saves by buying the cheaper lens
    savings = price_with_discount - cheaper_lense_cost
    result = savings
    return result

print(solution())