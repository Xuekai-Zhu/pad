def solution():
    
    sandwiches_per_person = 2
    people_on_committee = 24
    croissants_per_sandwich = 1  
    croissants_per_dozen = 12
    cost_per_dozen = 8
    total_sandwiches = sandwiches_per_person * people_on_committee
    total_croissants = total_sandwiches * croissants_per_sandwich
    dozens_needed = total_croissants / croissants_per_dozen

    
    if dozens_needed != int(dozens_needed):
        dozens_needed = int(dozens_needed) + 1

    total_cost = dozens_needed * cost_per_dozen
    result = total_cost
    return result

print(solution())