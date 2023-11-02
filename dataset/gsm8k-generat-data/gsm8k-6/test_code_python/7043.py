def solution():
    # Calculate how much Stephanie still needs to pay for her bills
    gas_bill_remaining = 40 - (40 * 0.75) - 5  # she paid 3/4 of gas bill and made another payment of $5
    water_bill_remaining = 40 - (40 * 0.5)  # she paid half of water bill
    internet_bill_remaining = 25 - 4*5  # she made 4 payments of $5 towards her internet bill

    total_remaining = gas_bill_remaining + water_bill_remaining + internet_bill_remaining

    result = total_remaining
    return result

print(solution())