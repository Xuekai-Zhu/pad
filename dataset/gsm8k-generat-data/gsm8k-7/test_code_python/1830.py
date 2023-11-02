def solution():
    num_people = 15
    ice_per_person = 2
    ice_per_bag = 10
    cost_per_bag = 3.0

    # Calculate the total amount of ice needed
    total_ice = num_people * ice_per_person

    # Calculate the total number of bags of ice needed
    total_bags = total_ice // ice_per_bag
    if total_ice % ice_per_bag != 0:
        total_bags += 1

    # Calculate the total cost of all the bags of ice
    total_cost = total_bags * cost_per_bag
    result = total_cost
    return result

print(solution())