def solution():
    """James has a room that is 13 feet by 18 feet. He increases each dimension by 2 feet. He then builds 3 more rooms of equal size and 1 room of twice that size. How much area does he have?"""
    original_area = 13 * 18
    new_dimension_1 = 15
    new_dimension_2 = 20
    new_area = new_dimension_1 * new_dimension_2
    total_area = (new_area * 3) + (new_area * 2)
    total_area += original_area
    result = total_area
    return result

print(solution())