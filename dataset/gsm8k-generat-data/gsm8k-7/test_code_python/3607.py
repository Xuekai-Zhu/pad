def solution():
    cost_per_gallon = 1
    water_needed_per_person = 0.5
    num_people = 6

    # Calculate the total water needed for the family for the day
    total_water_needed = num_people * water_needed_per_person

    # Calculate the total cost for fresh water for the day
    total_cost = total_water_needed * cost_per_gallon
    result = total_cost
    return result

print(solution())