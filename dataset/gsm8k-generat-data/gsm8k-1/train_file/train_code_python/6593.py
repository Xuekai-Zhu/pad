def solution():
    """Max needs 65 paper plates for the barbecue party. He already has 22 green paper plates and 24 blue paper plates. How many more paper plates does he need?"""
    total_needed = 65
    green_plates = 22
    blue_plates = 24
    plates_needed = total_needed - green_plates - blue_plates
    result = plates_needed
    return result

print(solution())