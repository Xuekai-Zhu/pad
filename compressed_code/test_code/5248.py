def solution():
    
    truck1 = 20 * 8
    truck2 = 12 * 8
    total_oil = truck1 * 7 + truck2 * 5
    containers_per_truck = total_oil // 10
    result = containers_per_truck
    return result

print(solution())