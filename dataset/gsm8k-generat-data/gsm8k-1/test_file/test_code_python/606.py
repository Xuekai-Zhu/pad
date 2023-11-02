def solution():
    """It costs $194 per meter to repave a street. Monica's street is 150 meters long. How much more does it cost to repave Lewis' street, which is 490 meters long?"""
    monica_street_length = 150
    lewis_street_length = 490
    cost_per_meter = 194
    monica_cost = monica_street_length * cost_per_meter
    lewis_cost = lewis_street_length * cost_per_meter
    difference = lewis_cost - monica_cost
    result = difference
    return result

print(solution())