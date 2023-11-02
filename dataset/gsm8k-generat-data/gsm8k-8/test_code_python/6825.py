def solution():
    # Find how many chocolate bars and soda cans Theresa bought in total
    total_chocolate_bars = 12
    total_soda_cans = 18

    # Divide by 2 to find how many Kayla bought
    kayla_chocolate_bars = total_chocolate_bars / 2
    kayla_soda_cans = total_soda_cans / 2

    # Add Kayla's purchases together
    kayla_total = kayla_chocolate_bars + kayla_soda_cans

    result = kayla_total
    return result

print(solution())