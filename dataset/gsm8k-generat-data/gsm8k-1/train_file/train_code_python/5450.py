def solution():
    """Carolyn is trimming a dress with lace around the cuffs, waist, hem, and neckline. Each cuff is 50 cm long, the hem is 300 cm long, 
    the waist is a third of the length of the hem, and the neck will have 5 ruffles that each use 20 cm of lace. 
    If lace costs $6/m, how much does Carolyn spend on lace?"""
    cuff_length = 50
    hem_length = 300
    waist_length = hem_length / 3
    ruffle_length = 5 * 20
    total_length = cuff_length * 2 + hem_length + waist_length + ruffle_length
    cost_per_meter = 6
    total_cost = total_length / 100 * cost_per_meter
    
    return total_cost

print(solution())