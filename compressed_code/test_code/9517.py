def solution():
    
    num_parents = 2
    num_brothers = 3
    num_brother_spouses = 3
    num_nieces_nephews = 6
    total_recipients = num_parents + num_brothers + num_brother_spouses + num_nieces_nephews
    cost_per_package = 5
    total_cost = total_recipients * cost_per_package
    result = total_cost
    return result

print(solution())