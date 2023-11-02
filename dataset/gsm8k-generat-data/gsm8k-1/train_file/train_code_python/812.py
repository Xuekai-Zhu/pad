def solution():
    """Tom cannot afford a normal doctor, so he goes to a discount clinic that is 70% cheaper. It takes two visits, though, instead of 1. A normal doctor charges $200 for a visit. How much money does he save?"""
    normal_cost = 200
    discount_percent = 70
    discount_cost = normal_cost * (100 - discount_percent) / 100
    total_cost = discount_cost * 2
    saved_amount = normal_cost * 2 - total_cost
    result = saved_amount
    
    return result

print(solution())