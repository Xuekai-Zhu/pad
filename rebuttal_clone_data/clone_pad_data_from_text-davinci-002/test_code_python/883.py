def solution():
    boxes_of_bolts = 7
    bolts_per_box = 11
    boxes_of_nuts = 3
    nuts_per_box = 15
    days_early = 6
    bolts_leftover = 3
    nuts_leftover = 6
    total_bolts = (boxes_of_bolts * bolts_per_box) - bolts_leftover
    total_nuts = (boxes_of_nuts * nuts_per_box) - nuts_leftover
    result = (total_bolts, total_nuts)
    return result

print(solution())