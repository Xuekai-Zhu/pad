def solution():
    cuff_length = 50  # Each cuff is 50cm long
    hem_length = 300  # The hem is 300cm long
    waist_length = hem_length / 3  # The waist is a third of the length of the hem
    neck_ruffles_length = 5 * 20  # The neck will have 5 ruffles that each use 20cm of lace
    total_length = cuff_length * 2 + hem_length + waist_length + neck_ruffles_length

    # Calculate the cost of the lace
    lace_cost_per_meter = 6  # Lace costs $6/m
    cost_of_lace = total_length / 100 * lace_cost_per_meter
    result = cost_of_lace
    return result

print(solution())