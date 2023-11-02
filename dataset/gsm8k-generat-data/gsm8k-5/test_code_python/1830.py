def solution():
    num_people = 15  # There will be 15 people at the BBQ
    ice_per_person = 2  # Chad needs 2 pounds of ice per person
    total_ice_needed = num_people * ice_per_person  # Total ice needed for all the guests
    bags_of_ice_needed = total_ice_needed / 10  # Each bag of ice contains 10 pounds

    # Round up to the nearest whole number of bags of ice
    bags_of_ice_needed = math.ceil(bags_of_ice_needed)

    # Calculate the total cost of ice
    cost_per_pack = 3.0  # Each pack costs $3.00
    packs_of_ice_needed = bags_of_ice_needed / 10  # Each pack contains 10 bags of ice
    total_cost = packs_of_ice_needed * cost_per_pack

    result = total_cost
    return result

print(solution())