def solution():
    """ Xavier needs 84 paper plates for a housewarming party. He already has 21 green plates and 28 red plates. How many more plates should Xavier buy?"""
    total_plates_needed = 84
    plates_on_hand = 21 + 28
    plates_to_buy = total_plates_needed - plates_on_hand
    result = plates_to_buy
    return result

print(solution())