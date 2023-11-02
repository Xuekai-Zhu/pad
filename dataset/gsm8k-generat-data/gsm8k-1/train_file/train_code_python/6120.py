def solution():
    """Carrie wants to take a trip to New York. She can get a 20% discount on an $850 flight with Delta Airlines. 
    She can also save 30% off an $1100 flight with United Airlines. How much money would she save by choosing the cheapest flight?"""
    
    delta_price = 850
    delta_discount = 0.2
    delta_savings = delta_price * delta_discount
    delta_final_price = delta_price - delta_savings
    
    united_price = 1100
    united_discount = 0.3
    united_savings = united_price * united_discount
    united_final_price = united_price - united_savings
    
    if delta_final_price < united_final_price:
        result = united_savings
    else:
        result = delta_savings
    
    return result

print(solution())