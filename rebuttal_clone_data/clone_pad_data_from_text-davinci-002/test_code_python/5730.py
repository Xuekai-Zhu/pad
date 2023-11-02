def solution():
    current_balance = 50
    interest_rate = 20
    interest_charge = current_balance * (interest_rate / 100)
    new_balance = current_balance + interest_charge
    second_interest_charge = new_balance * (interest_rate / 100)
    updated_balance = new_balance + second_interest_charge
    result = updated_balance
    
    return result

print(solution())