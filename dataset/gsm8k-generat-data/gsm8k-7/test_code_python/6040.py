def solution():
    total_flyers = 1236
    jack_flyers = 120
    rose_flyers = 320

    # Calculate the total number of flyers handed out
    total_handed_out = jack_flyers + rose_flyers

    # Calculate the number of flyers left to hand out
    left_to_hand_out = total_flyers - total_handed_out
    result = left_to_hand_out
    return result

print(solution())