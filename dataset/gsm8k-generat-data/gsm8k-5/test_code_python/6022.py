def solution():
    total_coconuts = 144  # Barbie and Bruno have 144 coconuts
    barbie_capacity = 4  # Barbie can carry 4 coconuts at a time
    bruno_capacity = 8  # Bruno can carry 8 coconuts at a time

    # Calculate how many trips Barbie and Bruno need to make together
    total_trips = 0
    while total_coconuts > 0:
        # Calculate how many coconuts they can carry together
        combined_capacity = barbie_capacity + bruno_capacity
        # Take as many coconuts as they can carry together
        taken_coconuts = min(combined_capacity, total_coconuts)
        # Update the total number of coconuts left to move
        total_coconuts -= taken_coconuts
        # Increase the trip count by 1
        total_trips += 1

    result = total_trips
    return result

print(solution())