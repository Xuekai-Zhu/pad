def solution():
    """Keanu's motorcycle can store 8 liters of gasoline. If his destination is 280 miles away and his motorcycle consumes 8 liters of gasoline per 40 miles, how many times does Keanu have to refill his motorcycle with gasoline if he will make a round trip?"""
    gas_capacity = 8
    distance_per_fillup = 40
    distance_per_trip = 280 * 2
    gas_per_trip = distance_per_trip / distance_per_fillup
    num_fillups_per_trip = gas_per_trip / gas_capacity
    result = num_fillups_per_trip
    return result

print(solution())