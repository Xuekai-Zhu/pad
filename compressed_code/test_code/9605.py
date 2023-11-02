def solution():
    
    num_people = 10
    chips_per_person = 1.2
    cost_per_pound = 0.25
    total_pounds = num_people * chips_per_person
    total_cost = total_pounds * cost_per_pound
    result = total_cost
    return result

print(solution())