def solution():
    cuff_length = 50
    hem_length = 300
    waist_length = hem_length / 3
    num_ruffles = 5
    ruffle_length = 20
    cost_per_meter = 6.0

    # Calculate the total length of lace needed for the cuffs
    cuffs_lace = cuff_length * 2

    # Calculate the total length of lace needed for the hem
    hem_lace = hem_length

    # Calculate the total length of lace needed for the waist
    waist_lace = waist_length * 2

    # Calculate the total length of lace needed for the ruffles
    ruffles_lace = num_ruffles * ruffle_length

    # Calculate the total length of lace needed
    total_lace = cuffs_lace + hem_lace + waist_lace + ruffles_lace

    # Calculate the total cost of the lace needed
    total_cost = (total_lace / 100) * cost_per_meter
    result = total_cost
    return result

print(solution())