def solution():
    # Calculate the length of the waist
    hem_length = 300
    waist_length = hem_length / 3

    # Calculate the total length of the lace needed
    cuff_length = 50 * 2
    hem_length = 300
    neck_length = 5 * 20
    total_lace_length = cuff_length + hem_length + waist_length + neck_length

    # Calculate the cost of the lace
    lace_cost_per_meter = 6
    lace_cost = total_lace_length * (lace_cost_per_meter/100)

    result = lace_cost
    return result

print(solution())