def solution():
    num_grey_birds = 40
    num_white_birds = num_grey_birds + 6
    total_birds = num_grey_birds + num_white_birds

    # After half the birds fly away
    remaining_birds = total_birds / 2
    result = remaining_birds
    return result

print(solution())