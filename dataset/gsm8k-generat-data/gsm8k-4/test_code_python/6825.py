def solution():
    """Kayla and Theresa went to buy some chocolate bars and soda cans. Theresa bought twice the number of chocolate bars and soda cans Kayla bought. If Theresa bought 12 chocolate bars and 18 soda cans, how many chocolate bars and soda cans did Kayla buy in total?"""
    # Define the number of chocolate bars and soda cans Theresa bought
    t_chocolate_bars = 12
    t_soda_cans = 18

    # Calculate the number of chocolate bars and soda cans Kayla bought
    k_chocolate_bars = t_chocolate_bars / 2
    k_soda_cans = t_soda_cans / 2

    # Calculate the total number of chocolate bars and soda cans Kayla bought
    total_chocolate_bars = k_chocolate_bars
    total_soda_cans = k_soda_cans

    # return the total number of chocolate bars and soda cans Kayla bought
    result = total_chocolate_bars + total_soda_cans
    return result

print(solution())