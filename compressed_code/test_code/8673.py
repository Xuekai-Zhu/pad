def solution():
    
    max_spending = 1000
    discount = 100
    percent_off = 20
    discounted_price = (max_spending - discount) * (100 - percent_off) / 100
    difference = max_spending - discounted_price
    result = difference
    
    return result

print(solution())