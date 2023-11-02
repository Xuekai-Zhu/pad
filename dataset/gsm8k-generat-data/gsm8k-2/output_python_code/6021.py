def solution():
    """Barbie and Bruno have a pile of 144 coconuts that they need to move from one side of their yard to the other side. Barbie can carry 4 coconuts at a time, while Bruno can carry 8 coconuts at a time. If they make trips together carrying their maximum number of coconuts each time, how many trips together would they need to make to move all of the coconuts?"""
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