def solution():
    
    subscription_cost = 80
    discount_percent = 45
    discount_amount = subscription_cost * (discount_percent/100)
    discounted_subscription_cost = subscription_cost - discount_amount
    result = discounted_subscription_cost
    return result

print(solution())