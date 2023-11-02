def solution():
    num_boxes_bolts = 7
    bolts_per_box = 11
    num_boxes_nuts = 3
    nuts_per_box = 15
    days_saved = 6
    bolts_leftover = 3
    nuts_leftover = 6

    # Calculate total number of bolts and nuts purchased
    total_bolts = num_boxes_bolts * bolts_per_box
    total_nuts = num_boxes_nuts * nuts_per_box

    # Calculate the total number of bolts and nuts used
    bolts_used = total_bolts - bolts_leftover
    nuts_used = total_nuts - nuts_leftover

    result = (bolts_used, nuts_used)
    return result

print(solution())