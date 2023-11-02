def solution():
    cost_per_gallon = 45
    area_to_be_painted = 1600
    area_covered_per_gallon = 400
    gallons_needed = area_to_be_painted / area_covered_per_gallon
    total_cost = cost_per_gallon * gallons_needed
    cost_per_person = total_cost / 2
    result = cost_per_person
    return result

print(solution())