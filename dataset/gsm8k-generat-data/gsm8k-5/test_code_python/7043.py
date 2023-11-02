def solution():
    # Calculate the amount Stephanie still needs to pay for her gas bill
    gas_bill_remaining = (40 * 0.25) - 5  # Three-quarter paid already, minus $5 paid while checking budget

    # Calculate the amount Stephanie still needs to pay for her water bill
    water_bill_remaining = 40 * 0.5  # Half of the bill remains unpaid

    # Calculate the amount Stephanie still needs to pay for her internet bill
    internet_bill_remaining = 25 - (4 * 5)  # 4 payments of $5 already made

    # Calculate the total amount Stephanie still needs to pay for all bills
    total_remaining = gas_bill_remaining + water_bill_remaining + internet_bill_remaining

    result = total_remaining
    return result

print(solution())