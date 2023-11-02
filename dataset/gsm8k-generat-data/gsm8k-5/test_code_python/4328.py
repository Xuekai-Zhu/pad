def solution():
    red_snapper_quantity = 8  # The fisherman gets 8 Red snappers every day
    tuna_quantity = 14  # The fisherman gets 14 Tunas every day
    red_snapper_price = 3  # A Red snapper costs $3
    tuna_price = 2  # A Tuna costs $2

    # Calculate the total earnings from Red snappers
    red_snapper_earnings = red_snapper_quantity * red_snapper_price

    # Calculate the total earnings from Tunas
    tuna_earnings = tuna_quantity * tuna_price

    # Calculate the total earnings per day
    total_earnings = red_snapper_earnings + tuna_earnings
    result = total_earnings
    return result

print(solution())