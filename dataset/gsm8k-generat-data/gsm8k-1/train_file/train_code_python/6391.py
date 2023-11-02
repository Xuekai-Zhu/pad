def solution():
    """Ariana is past due on three bills. The first bill for $200 charges 10% simple interest for each overdue month and it's 2 months overdue. The second bill for $130 charges a flat $50 late fee per month and is 6 months overdue. The last bill is two months late and charges a $40 fee the first month overdue and twice that fee the second month overdue and is for $444. How much does Ariana owe in total?"""
    bill1_amount = 200
    bill1_interest_rate = 0.1
    bill1_overdue_months = 2
    bill1_interest = bill1_amount * bill1_interest_rate * bill1_overdue_months
    bill1_total = bill1_amount + bill1_interest

    bill2_amount = 130
    bill2_late_fee = 50
    bill2_overdue_months = 6
    bill2_fee = bill2_late_fee * bill2_overdue_months
    bill2_total = bill2_amount + bill2_fee

    bill3_amount = 444
    bill3_first_month_fee = 40
    bill3_second_month_fee = bill3_first_month_fee * 2
    bill3_overdue_months = 2
    bill3_fee = bill3_first_month_fee + bill3_second_month_fee
    bill3_total = bill3_amount + bill3_fee

    total_owed = bill1_total + bill2_total + bill3_total
    result = total_owed
    return result

print(solution())