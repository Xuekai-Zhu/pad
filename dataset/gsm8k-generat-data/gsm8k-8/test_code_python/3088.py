def solution():
    # Calculate how many liters of gasoline Keanu needs for one way
    one_way_gas = 280/40 * 8/8
    # Calculate how many liters of gasoline Keanu needs for a round trip
    round_trip_gas = one_way_gas * 2
    # Calculate how many times Keanu needs to refill his motorcycle
    refills = round_trip_gas/8
    result = refills
    return result

print(solution())