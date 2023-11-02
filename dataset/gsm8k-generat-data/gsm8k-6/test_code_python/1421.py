def solution():
    # Calculate the number of plates Xavier needs to buy
    total_plates = 84
    plates_on_hand = 21 + 28  # plates Xavier already has
    plates_to_buy = total_plates - plates_on_hand
    result = plates_to_buy
    return result

print(solution())