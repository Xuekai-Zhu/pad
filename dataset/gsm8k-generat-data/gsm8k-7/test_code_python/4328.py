def solution():
    num_red_snappers = 8
    red_snapper_price = 3

    num_tunas = 14
    tuna_price = 2

    # Calculate the total earnings from Red snappers
    red_snapper_earnings = num_red_snappers * red_snapper_price

    # Calculate the total earnings from Tunas
    tuna_earnings = num_tunas * tuna_price

    # Calculate the total earnings
    total_earnings = red_snapper_earnings + tuna_earnings
    result = total_earnings
    return result

print(solution())