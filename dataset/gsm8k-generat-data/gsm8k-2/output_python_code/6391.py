def solution():
    """Ariana is past due on three bills. The first bill for $200 charges 10% simple interest for each overdue month and it's 2 months overdue. 
    The second bill for $130 charges a flat $50 late fee per month and is 6 months overdue. 
    The last bill is two months late and charges a $40 fee the first month overdue and twice that fee the second month overdue and is for $444. 
    How much does Ariana owe in total?"""
    # First bill calculation
    first_bill_principal = 200
    first_bill_interest_rate = 0.1
    first_bill_months_overdue = 2
    first_bill_interest = first_bill_principal * first_bill_interest_rate * first_bill_months_overdue
    first_bill_total = first_bill_principal + first_bill_interest

    # Second bill calculation
    second_bill_principal = 130
    second_bill_months_overdue = 6
    second_bill_late_fee = 50
    second_bill_total = second_bill_principal + (second_bill_months_overdue * second_bill_late_fee)

    # Third bill calculation
    third_bill_months_overdue = 2
    third_bill_fees = 0
    for i in range(third_bill_months_overdue):
        if i == 0:
            third_bill_fees += 40
        else:
            third_bill_fees += 80
    third_bill_total = 444 + third_bill_fees

    # Total calculation
    total = first_bill_total + second_bill_total + third_bill_total
    result = total
    return result

print(solution())