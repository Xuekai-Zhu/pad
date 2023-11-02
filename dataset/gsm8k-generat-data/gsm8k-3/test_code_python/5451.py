def solution():
    """Carolyn is trimming a dress with lace around the cuffs, waist, hem, and neckline. Each cuff is 50 cm long, the hem is 300 cm long, the waist is a third of the length of the hem, and the neck will have 5 ruffles that each use 20 cm of lace. If lace costs $6/m, how much does Carolyn spend on lace?"""
    # Define the length of each part of the dress
    cuff_length = 50
    hem_length = 300
    waist_length = hem_length/3
    neck_ruffles = 5
    ruffle_length = 20

    # Calculate the total length of lace needed
    total_length = cuff_length*2 + hem_length + waist_length + neck_ruffles*ruffle_length

    # Calculate the total cost of the lace
    lace_cost = total_length/100 * 6

    # Display the total cost of the lace
    result = lace_cost
    return result

print(solution())