def solution():
    
    total_earned = 30
    cost_per_person = 2.5
    number_of_people = 10
    total_cost = cost_per_person * number_of_people
    amount_left = total_earned - total_cost
    result = amount_left
    return result

print(solution())