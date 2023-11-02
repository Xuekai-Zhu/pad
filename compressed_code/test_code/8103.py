def solution():
    
    meat_per_person = 0.5
    num_people = 6
    price_per_pound = 15.00
    total_meat = meat_per_person * num_people
    total_cost = total_meat * price_per_pound
    result = total_cost
    return result

print(solution())