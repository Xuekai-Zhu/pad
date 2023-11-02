def solution():
    blocks_to_bus_stop = 4
    bus_to_library = 7
    
    # Calculate the total blocks traveled to get to the library
    to_library = blocks_to_bus_stop + bus_to_library
    
    # Calculate the total blocks traveled round trip
    round_trip = to_library * 2
    
    result = round_trip
    return result

print(solution())