def solution():
    num_pots_made = 80
    frac_pots_cracked = 2/5
    pot_price = 40

    # Calculate the number of pots that were not cracked
    num_pots_not_cracked = num_pots_made * (1 - frac_pots_cracked)

    # Calculate the total amount of money made from selling the non-cracked pots
    total_money_made = num_pots_not_cracked * pot_price
    result = total_money_made
    return result

print(solution())