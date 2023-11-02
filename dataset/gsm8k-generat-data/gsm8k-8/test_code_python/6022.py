def solution():
    # Define the number of coconuts and the carrying capacities of Barbie and Bruno
    num_coconuts = 144
    barbie_capacity = 4
    bruno_capacity = 8

    # Calculate the total number of trips needed, rounding up to the nearest integer
    total_trips = math.ceil(num_coconuts / (barbie_capacity + bruno_capacity))

    result = total_trips
    return result

print(solution())