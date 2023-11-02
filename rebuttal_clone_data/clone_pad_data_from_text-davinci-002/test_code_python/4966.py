def solution():
    first_transfer = 90
    first_transfer_charge = first_transfer * 0.02
    second_transfer = 60
    second_transfer_charge = second_transfer * 0.02
    total_charges = first_transfer_charge + second_transfer_charge
    balance = 400 - (first_transfer + second_transfer + total_charges)
    reversed_balance = balance + (second_transfer - second_transfer_charge)
    result = reversed_balance
    return result

print(solution())