def solution():
    """The fisherman gets 8 Red snappers and 14 Tunas every day. If a Red snapper costs $3 and a Tuna costs $2, how much does he earn every day?"""
    # Define the number of Red snappers and Tunas caught each day
    red_snappers = 8
    tunas = 14

    # Define the price per Red snapper and Tuna
    red_snapper_price = 3
    tuna_price = 2

    # Calculate the total earnings from catching Red snappers and Tunas
    earnings = (red_snappers * red_snapper_price) + (tunas * tuna_price)

    # return the result
    result = earnings
    return result

print(solution())