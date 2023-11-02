def solution():
    
    adults_per_hour = 4
    children_per_hour = 3
    adult_cost = 50
    child_cost = 25
    total_hours = 8
    total_adults = adults_per_hour * total_hours
    total_children = children_per_hour * total_hours
    total_money = (total_adults * adult_cost) + (total_children * child_cost)
    result = total_money
    return result

print(solution())