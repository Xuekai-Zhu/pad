def solution():
    # Calculate how many chocolate bars Kayla bought
    kayla_choco_bars = 12 / 2 
    # Since Theresa bought twice as many as Kayla, Kayla bought half as many as Theresa
    theresa_choco_bars = 12
    # Total number of chocolate bars Kayla bought
    total_choco_bars = kayla_choco_bars + theresa_choco_bars

    # Calculate how many soda cans Kayla bought
    kayla_soda_cans = 18 / 2
    # Since Theresa bought twice as many as Kayla, Kayla bought half as many as Theresa
    theresa_soda_cans = 18
    # Total number of soda cans Kayla bought
    total_soda_cans = kayla_soda_cans + theresa_soda_cans

    # Calculate the total number of chocolate bars and soda cans Kayla bought
    total_bars_cans = total_choco_bars + total_soda_cans
    result = total_bars_cans
    return result

print(solution())