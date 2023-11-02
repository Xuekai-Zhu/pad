def solution():
    # Calculate the total length of lace needed
    cuff_length = 50 * 2  # there are two cuffs
    waist_length = 300/3
    neck_length = 5 * 20

    total_lace_length = cuff_length + waist_length + neck_length + 300  # lace needed for all parts of the dress
    lace_cost_per_meter = 6
    total_lace_cost = lace_cost_per_meter * (total_lace_length/100)  # convert cm to meters

    result = total_lace_cost
    return result

print(solution())