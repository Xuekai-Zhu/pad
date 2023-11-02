def solution():
    """James has a room that is 13 feet by 18 feet. He increases each dimension by 2 feet. He then builds 3 more rooms of equal size and 1 room of twice that size. How much area does he have?"""
    
    original_length = 13
    original_width = 18
    increased_length = original_length + 2
    increased_width = original_width + 2
    area_original_room = original_length * original_width
    area_increased_room = increased_length * increased_width
    total_area = (area_increased_room + 3*area_increased_room + 2*area_increased_room)
    result = total_area
    
    return result

print(solution())