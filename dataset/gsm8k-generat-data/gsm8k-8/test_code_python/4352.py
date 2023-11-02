def solution():
    # Calculate cost of tablecloths
    tablecloth_cost = 20 * 25

    # Calculate cost of place settings
    place_setting_cost = 4 * 20 * 10

    # Calculate cost of centerpieces
    rose_cost = 20 * 10 * 5
    lily_cost = 20 * 15 * 4
    centerpiece_cost = rose_cost + lily_cost

    # Calculate total cost
    total_cost = tablecloth_cost + place_setting_cost + centerpiece_cost

    result = total_cost
    return result

print(solution())