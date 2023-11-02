def solution():
    num_snickers = 2
    snickers_price = 1.5

    num_mms_packs = 3
    mms_pack_price = snickers_price * 2

    total_cost = (num_snickers * snickers_price) + (num_mms_packs * mms_pack_price)

    amount_given = 20  # Julia gave the cashier 2 $10 bills
    change = amount_given - total_cost
    result = change
    return result

print(solution())