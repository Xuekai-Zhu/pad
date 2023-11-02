def solution():
    """There are 7 trucks that have 20 boxes. There are 5 trucks that have 12 boxes. Each box holds 8 containers of oil. If all of the oil is evenly redistributed onto 10 trucks, how many containers of oil will each truck have?"""
    truck1 = 20 * 8
    truck2 = 12 * 8
    total_oil = truck1 * 7 + truck2 * 5
    containers_per_truck = total_oil // 10
    result = containers_per_truck
    return result

print(solution())