def solution():
    """Barbie and Bruno have a pile of 144 coconuts that they need to move from one side of their yard to the other side.  Barbie can carry 4 coconuts at a time, while Bruno can carry 8 coconuts at a time.  If they make trips together carrying their maximum number of coconuts each time, how many trips together would they need to make to move all of the coconuts?"""
    # Define the number of coconuts that Barbie and Bruno can carry each trip
    BARBIE_CAPACITY = 4
    BRUNO_CAPACITY = 8

    # Define the total number of coconuts that need to be moved
    total_coconuts = 144

    # Calculate the number of trips needed
    rounds = (total_coconuts // (BARBIE_CAPACITY + BRUNO_CAPACITY))
    if total_coconuts % (BARBIE_CAPACITY + BRUNO_CAPACITY) != 0:
        rounds += 1

    # Display the number of trips needed
    result = rounds
    return result

print(solution())