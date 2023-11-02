def solution():
    sandwiches_per_person = 2
    people_on_committee = 24
    croissants_per_package = 12
    cost_per_package = 8
    
    total_sandwiches_needed = sandwiches_per_person * people_on_committee
    total_croissants_needed = total_sandwiches_needed / 2
    total_packages_needed = total_croissants_needed / croissants_per_package
    total_cost = total_packages_needed * cost_per_package
    
    result = total_cost
    return result

print(solution())