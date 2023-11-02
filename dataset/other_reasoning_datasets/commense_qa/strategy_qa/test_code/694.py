def solution():
    is_bitcoin_tangible = True
    is_bitcoin_stored_in_hard_wallet = True
    hard_wallet_size = "thumb drive"
    fits_in_pocket = True
    if is_bitcoin_tangible and is_bitcoin_stored_in_hard_wallet and hard_wallet_size == "thumb drive" and fits_in_pocket:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())