def solution():
    """Keanu's motorcycle can store 8 liters of gasoline. If his destination is 280 miles away and his motorcycle consumes 8 liters of gasoline per 40 miles, how many times does Keanu have to refill his motorcycle with gasoline if he will make a round trip?"""
    total_distance = 560 # round trip
    gas_capacity = 8
    gas_consumption = 8 # per 40 miles
    refills = total_distance // 40 // (gas_capacity // gas_consumption)
    result = refills
    return result

print(solution())