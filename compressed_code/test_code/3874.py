def solution():
    
    original_price = 40
    discount = 0.25
    discounted_price = original_price * (1 - discount)
    num_people = 5
    total_cost = num_people * discounted_price
    result = total_cost
    return result

print(solution())