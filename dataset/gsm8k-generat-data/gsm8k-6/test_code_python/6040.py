def solution():
    # Calculate the number of flyers left to be handed out
    total_flyers = 1236
    flyers_handed = 120 + 320
    flyers_left = total_flyers - flyers_handed
    result = flyers_left
    return result

print(solution())