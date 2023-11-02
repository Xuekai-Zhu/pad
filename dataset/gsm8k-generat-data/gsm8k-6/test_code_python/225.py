def solution():
    # Calculate the total number of gallons of water needed
    gallons_heavy = 20 * 2  # Two heavy wash loads
    gallons_regular = 10 * 3  # Three regular wash loads
    gallons_light = 2 * 2  # Two light wash loads (one of which is bleached, so an extra light wash cycle is added)
    total_gallons = gallons_heavy + gallons_regular + gallons_light
    result = total_gallons
    return result

print(solution())