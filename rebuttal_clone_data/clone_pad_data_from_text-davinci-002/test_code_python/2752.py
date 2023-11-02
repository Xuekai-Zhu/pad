def solution():
    library_percentage = 15
    parks_percentage = 24
    library_cost = 3000
    parks_cost = library_cost * (parks_percentage / 100)
    total_cost = library_cost + parks_cost
    remaining_budget = 1 - (total_cost / library_cost)
    result = remaining_budget
    
    return result

print(solution())