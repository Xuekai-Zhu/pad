def solution():
    
    cuff_length = 50
    hem_length = 300
    waist_length = hem_length / 3
    neck_ruffles = 5
    ruffle_length = 20

    total_length = 2 * cuff_length + hem_length + waist_length + (neck_ruffles * ruffle_length)
    total_lace_cost = (total_length/100) * 6

    result = total_lace_cost
    return result

print(solution())