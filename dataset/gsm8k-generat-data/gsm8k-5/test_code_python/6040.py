def solution():
    total_flyers = 1236  # Jack and Rose made 1236 flyers to hand out
    flyers_handed = 120 + 320  # Jack handed 120 and Rose handed 320 flyers

    # Calculate the number of flyers left to be handed out
    flyers_left = total_flyers - flyers_handed
    result = flyers_left
    return result

print(solution())