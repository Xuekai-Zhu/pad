def solution():
    # Angela's kitchen supplies
    pots_angela = 20
    plates_angela = 3 * pots_angela + 6
    cutlery_angela = 0.5 * plates_angela

    # Sharon's kitchen supplies
    pots_sharon = 0.5 * pots_angela
    plates_sharon = 3 * plates_angela - 20
    cutlery_sharon = 2 * cutlery_angela

    # Total number of kitchen supplies Sharon wants to buy
    total_supplies = pots_sharon + plates_sharon + cutlery_sharon
    result = total_supplies
    return result

print(solution())