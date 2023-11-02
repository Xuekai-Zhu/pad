def solution():
    # Calculate the number of pots Angela has
    pots_angela = 20  # given in the problem
    # Calculate the number of plates Angela has
    plates_angela = (pots_angela * 3) + 6  # given in the problem
    # Calculate the number of cutlery Angela has
    cutlery_angela = plates_angela / 2  # given in the problem
    # Calculate the number of pots Sharon wants to buy
    pots_sharon = pots_angela / 2  # given in the problem
    # Calculate the number of plates Sharon wants to buy
    plates_sharon = (3 * plates_angela) - 20  # given in the problem
    # Calculate the number of cutlery Sharon wants to buy
    cutlery_sharon = 2 * cutlery_angela  # given in the problem
    # Calculate the total number of kitchen supplies Sharon wants to buy
    total_supplies = pots_sharon + plates_sharon + cutlery_sharon
    result = total_supplies
    return result

print(solution())