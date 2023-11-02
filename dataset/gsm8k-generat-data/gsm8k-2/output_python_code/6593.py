def solution():
    """Max needs 65 paper plates for the barbecue party. He already has 22 green paper plates and 24 blue paper plates. How many more paper plates does he need?"""
    plates_needed = 65
    green_plates = 22
    blue_plates = 24
    total_plates = green_plates + blue_plates
    plates_to_buy = plates_needed - total_plates
    result = plates_to_buy
    return result

print(solution())