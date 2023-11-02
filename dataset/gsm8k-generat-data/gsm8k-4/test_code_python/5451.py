def solution():
    """Carolyn is trimming a dress with lace around the cuffs, waist, hem, and neckline. Each cuff is 50 cm long, the hem is 300 cm long, the waist is a third of the length of the hem, and the neck will have 5 ruffles that each use 20 cm of lace. If lace costs $6/m, how much does Carolyn spend on lace?"""
    # Define the length of each cuff and the length of the hem
    cuff_length = 50
    hem_length = 300

    # Calculate the length of the waist
    waist_length = hem_length / 3

    # Calculate the length of lace needed for the cuffs
    cuff_lace = cuff_length * 2

    # Calculate the length of lace needed for the hem
    hem_lace = hem_length

    # Calculate the length of lace needed for the waist
    waist_lace = waist_length * 2

    # Calculate the length of lace needed for the 5 ruffles
    ruffle_lace = 5 * 20

    # Calculate the total length of lace needed
    total_lace = cuff_lace + hem_lace + waist_lace + ruffle_lace

    # Calculate the cost of the lace
    lace_cost = total_lace / 100 * 6

    # Return the result
    result = lace_cost
    return result

print(solution())