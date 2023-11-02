def solution():
    """Kayla and Theresa went to buy some chocolate bars and soda cans. Theresa bought twice the number of chocolate bars and soda cans Kayla bought. If Theresa bought 12 chocolate bars and 18 soda cans, how many chocolate bars and soda cans did Kayla buy in total?"""
    theresa_chocolate = 12
    theresa_soda = 18
    kayla_chocolate = theresa_chocolate / 2
    kayla_soda = theresa_soda / 2
    total_chocolate = kayla_chocolate + theresa_chocolate
    total_soda = kayla_soda + theresa_soda
    result = total_chocolate + total_soda
    return result

print(solution())