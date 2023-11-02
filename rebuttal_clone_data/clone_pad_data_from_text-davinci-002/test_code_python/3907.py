def solution():
    fence_cost = 120000
    length_of_one_side = 5000
    perimeter = length_of_one_side * 4
    cost_of_one_meter = 30
    fenceable_meters = fence_cost / cost_of_one_meter
    nonfenceable_meters = perimeter - fenceable_meters
    nonfenceable_feet = nonfenceable_meters / 0.3048
    result = nonfenceable_feet
    return result

print(solution())