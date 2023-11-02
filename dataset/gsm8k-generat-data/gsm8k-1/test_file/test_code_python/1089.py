def solution():
    """Tony is painting a room with four walls. The north and south walls are 10 x 8 feet. The east and west walls are 5 x 8 feet. A gallon of paint can cover 20 square feet and cost $12. How much will it cost to paint the room?"""
    area_north_south = 10 * 8 * 2
    area_east_west = 5 * 8 * 2
    total_area = area_north_south + area_east_west
    gallons_needed = total_area / 20
    cost = gallons_needed * 12
    result = cost
    return result

print(solution())