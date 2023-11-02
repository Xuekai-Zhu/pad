def solution():
    """Tyrion changes his face mask two times every time he goes out. If he goes out three times a day, how many face masks does he use every 2 days?"""
    masks_per_outing = 2
    outings_per_day = 3
    days = 2
    total_outings = outings_per_day * days
    total_masks = total_outings * masks_per_outing
    result = total_masks
    return result

print(solution())