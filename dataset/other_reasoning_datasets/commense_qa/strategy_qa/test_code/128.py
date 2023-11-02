def solution():
    northern_waters = ["Arctic Ocean", "North Atlantic", "Bering Sea", "North Pacific"]
    southern_hemisphere = ["New Zealand"]
    traditional_boats = ["canoes"]
    if any(water in northern_waters for water in southern_hemisphere) and "kayak" not in traditional_boats:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())