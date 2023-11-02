def solution():
    
    num_bills = 3
    bill_value = 20
    current_wallet_value = 75
    new_wallet_value = current_wallet_value + (num_bills * bill_value)
    result = new_wallet_value
    return result

print(solution())