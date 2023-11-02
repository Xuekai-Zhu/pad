def solution():
    """Barbie and Bruno have a pile of 144 coconuts that they need to move from one side of their yard to the other side. 
    Barbie can carry 4 coconuts at a time, while Bruno can carry 8 coconuts at a time. 
    If they make trips together carrying their maximum number of coconuts each time, how many trips together would they need to make to move all of the coconuts?"""
    # Define the total number of coconuts and the number each person can carry
    total_coconuts = 144
    barbie_coconuts = 4
    bruno_coconuts = 8

    # Determine the number of trips required for each person alone
    barbie_trips = total_coconuts // barbie_coconuts
    bruno_trips = total_coconuts // bruno_coconuts

    # Determine the number of trips required when they carry maximum coconuts together
    trips_together = total_coconuts // (barbie_coconuts + bruno_coconuts)

    # Add additional trips for remaining coconuts
    remaining_coconuts = total_coconuts % (barbie_coconuts + bruno_coconuts)
    if remaining_coconuts > 0:
        trips_together += 1

    # return the result
    result = trips_together
    return result

print(solution())