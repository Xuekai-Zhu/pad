def solution():
    # Define the number of people and amount of ice needed
    num_people = 15
    ice_per_person = 2
    total_ice_needed = num_people * ice_per_person

    # Calculate the number of ice bags needed
    ice_bags_needed = total_ice_needed / 10
    if ice_bags_needed.is_integer():
        ice_bags_needed = int(ice_bags_needed)
    else:
        ice_bags_needed = int(ice_bags_needed) + 1

    # Calculate the total cost of ice bags
    cost_per_pack = 3.00
    cost_per_ice_bag = cost_per_pack / 10
    total_cost = ice_bags_needed * cost_per_pack
    result = total_cost
    return result

print(solution())