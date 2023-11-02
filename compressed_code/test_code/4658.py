def solution():
    
    total_coconuts = 144
    barbie_capacity = 4
    bruno_capacity = 8
    total_capacity = barbie_capacity + bruno_capacity
    trips = total_coconuts // total_capacity
    if total_coconuts % total_capacity != 0:
        trips += 1
    result = trips
    return result

print(solution())