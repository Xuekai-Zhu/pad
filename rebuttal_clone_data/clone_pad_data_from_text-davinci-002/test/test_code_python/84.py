def solution():
    
    percent_discount = 45
    normal_cost = 80
    discount = normal_cost * (percent_discount / 100)
    discounted_cost = normal_cost - discount
    result = discounted_cost
    return result

print(solution())