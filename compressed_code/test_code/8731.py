def solution():
    
    price_per_pound = 3
    minimum_purchase = 15
    total_spent = 105
    pounds_purchased = (total_spent / price_per_pound)
    pounds_over_minimum = pounds_purchased - minimum_purchase
    result = pounds_over_minimum
    return result

print(solution())