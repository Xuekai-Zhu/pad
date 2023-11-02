def solution():
    
    
    first_bill_principal = 200
    first_bill_interest_rate = 0.1
    first_bill_months_overdue = 2
    first_bill_interest = first_bill_principal * first_bill_interest_rate * first_bill_months_overdue
    first_bill_total = first_bill_principal + first_bill_interest

    
    second_bill_principal = 130
    second_bill_months_overdue = 6
    second_bill_late_fee = 50
    second_bill_total = second_bill_principal + (second_bill_months_overdue * second_bill_late_fee)

    
    third_bill_months_overdue = 2
    third_bill_fees = 0
    for i in range(third_bill_months_overdue):
        if i == 0:
            third_bill_fees += 40
        else:
            third_bill_fees += 80
    third_bill_total = 444 + third_bill_fees

    
    total = first_bill_total + second_bill_total + third_bill_total
    result = total
    return result

print(solution())