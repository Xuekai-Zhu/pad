def solution():
    initial_balance = 800
    rent = 450
    paycheck = 1500
    electricity_bill = 117
    internet_bill = 100
    phone_bill = 70

    # Calculate the total amount spent
    total_spent = rent + electricity_bill + internet_bill + phone_bill

    # Calculate the total amount deposited
    total_deposited = paycheck

    # Calculate the final balance
    final_balance = initial_balance + total_deposited - total_spent

    result = final_balance
    return result

print(solution())