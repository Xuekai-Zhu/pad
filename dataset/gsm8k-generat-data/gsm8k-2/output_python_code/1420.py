def solution():
    """Xavier needs 84 paper plates for a housewarming party. He already has 21 green plates and 28 red plates. How many more plates should Xavier buy?"""
    total_plates = 84
    green_plates = 21
    red_plates = 28
    plates_needed = total_plates - green_plates - red_plates
    result = plates_needed
    return result

print(solution())