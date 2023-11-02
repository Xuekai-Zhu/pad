def solution():
    
    regular_rate = 40.00
    discount_percent = 25
    discounted_rate = regular_rate - (regular_rate * (discount_percent / 100))
    num_people = 5
    total_cost = discounted_rate * num_people
    result = total_cost
    return result

print(solution())