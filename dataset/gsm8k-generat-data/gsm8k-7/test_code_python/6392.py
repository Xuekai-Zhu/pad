def solution():
    # First bill
    bill1_amount = 200
    bill1_overdue_months = 2
    bill1_interest_rate = 0.10  # 10% per overdue month
    bill1_interest = bill1_amount * bill1_interest_rate * bill1_overdue_months
    total_bill1 = bill1_amount + bill1_interest

    # Second bill
    bill2_amount = 130
    bill2_overdue_months = 6
    bill2_late_fee = 50
    bill2_total_late_fee = bill2_late_fee * bill2_overdue_months
    total_bill2 = bill2_amount + bill2_total_late_fee

    # Third bill
    bill3_amount = 444
    bill3_overdue_months = 2
    bill3_late_fee_month1 = 40
    bill3_late_fee_month2 = 2 * bill3_late_fee_month1
    total_bill3 = bill3_amount + bill3_late_fee_month1 + bill3_late_fee_month2

    # Calculate total amount owed
    total_owed = total_bill1 + total_bill2 + total_bill3
    result = total_owed
    return result

print(solution())