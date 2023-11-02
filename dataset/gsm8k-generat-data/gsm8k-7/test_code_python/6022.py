def solution():
    num_coconuts = 144
    barbie_capacity = 4
    bruno_capacity = 8

    # Calculate the total number of trips needed
    total_trips = num_coconuts // (barbie_capacity + bruno_capacity)
    if num_coconuts % (barbie_capacity + bruno_capacity) != 0:
        total_trips += 1

    result = total_trips
    return result

print(solution())