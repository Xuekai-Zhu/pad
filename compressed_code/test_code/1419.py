def solution():
    
    people = 15
    ice_per_person = 2
    total_ice = people * ice_per_person
    ice_bags = total_ice / 10
    if ice_bags.is_integer():
        ice_bags = int(ice_bags)
    else:
        ice_bags = int(ice_bags) + 1
    cost_per_ice_bag = 3
    total_cost = ice_bags * cost_per_ice_bag
    result = total_cost
    return result

print(solution())