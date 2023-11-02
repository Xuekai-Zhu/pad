def solution():
    tuesday_balance = 800
    rent_payment = 450
    thursday_deposit = 1500
    electricity_bill = 117
    internet_bill = 100
    phone_bill = 70

    # Calculate Liza's balance after paying rent
    wednesday_balance = tuesday_balance - rent_payment

    # Calculate Liza's balance after depositing paycheck
    thursday_balance = wednesday_balance + thursday_deposit

    # Calculate Liza's balance after paying electricity and internet bills
    friday_balance = thursday_balance - electricity_bill - internet_bill

    # Calculate Liza's balance after paying phone bill
    saturday_balance = friday_balance - phone_bill

    result = saturday_balance
    return result

print(solution())