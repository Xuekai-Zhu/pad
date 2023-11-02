def solution():
    truck_capacity = 13500
    boxes_weight = 100 * 100
    crates_weight = 10 * 60
    sacks_weight = 50 * 50
    total_weight = boxes_weight + crates_weight + sacks_weight
    available_weight = truck_capacity - total_weight
    bags_weight = 40
    result = available_weight / bags_weight
    return result

print(solution())