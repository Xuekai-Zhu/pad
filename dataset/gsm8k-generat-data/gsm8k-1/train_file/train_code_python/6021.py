def solution():
    """Barbie and Bruno have a pile of 144 coconuts that they need to move from one side of their yard to the other side. Barbie can carry 4 coconuts at a time, while Bruno can carry 8 coconuts at a time. If they make trips together carrying their maximum number of coconuts each time, how many trips together would they need to make to move all of the coconuts?"""
    total_coconuts = 144
    barbie_coconuts = 4
    bruno_coconuts = 8
    combined_coconuts = barbie_coconuts + bruno_coconuts
    total_trips = total_coconuts // combined_coconuts + (total_coconuts % combined_coconuts > 0)
    result = total_trips
    return result

print(solution())