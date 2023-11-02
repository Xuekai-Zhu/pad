def solution():
    
    cost_per_gallon = 1
    gallons_per_person = 0.5
    num_people = 6
    total_gallons = gallons_per_person * num_people
    total_cost = total_gallons * cost_per_gallon
    result = total_cost
    return result

print(solution())