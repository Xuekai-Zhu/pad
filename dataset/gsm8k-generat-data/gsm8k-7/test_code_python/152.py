def solution():
    subscription_price = 80
    discount_percentage = 0.45 # 45% discount
    
    # Calculate the discounted price
    discounted_price = subscription_price * (1 - discount_percentage)
    
    result = discounted_price
    return result

print(solution())