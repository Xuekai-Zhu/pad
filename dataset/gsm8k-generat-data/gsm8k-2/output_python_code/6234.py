def solution():
    """Samson is going to another town which is 140 km away. He will use his car that uses ten liters of gasoline for a distance of 70 km. How many liters of gasoline will Samson need for a one-way trip?"""
    distance = 140
    one_way_distance = distance / 2
    gas_per_km = 10 / 70
    gas_needed = gas_per_km * one_way_distance
    result = gas_needed
    return result

print(solution())