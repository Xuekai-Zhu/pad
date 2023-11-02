def solution():
    # Calculate the number of trips needed to move all the coconuts
    total_coconuts = 144
    barbie_capacity = 4
    bruno_capacity = 8

    # Calculate the number of trips Barbie and Bruno need to make together
    trips_needed = (total_coconuts // (barbie_capacity + bruno_capacity)) + 1
    result = trips_needed
    return result

print(solution())