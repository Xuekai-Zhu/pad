def solution():
    # Define the width of the Golden Gate Bridge, a baker's dozen, and the width of a Mac truck
    bridge_width = 90
    baker_dozen = 13
    mac_truck_width = 8
    # Check if a baker's dozen of side by side Mac trucks would exceed the width of the bridge
    if baker_dozen * mac_truck_width > bridge_width:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())