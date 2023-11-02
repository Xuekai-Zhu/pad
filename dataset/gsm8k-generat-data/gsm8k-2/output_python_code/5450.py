def solution():
    """Carolyn is trimming a dress with lace around the cuffs, waist, hem, and neckline. Each cuff is 50 cm long, the hem is 300 cm long, the waist is a third of the length of the hem, and the neck will have 5 ruffles that each use 20 cm of lace. If lace costs $6/m, how much does Carolyn spend on lace?"""
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