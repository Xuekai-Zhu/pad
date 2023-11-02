def solution():
    # Calculate the total amount owed on each bill separately
    bill1 = 200 + (200 * 0.10 * 2)  # $200 bill charged 10% simple interest for 2 months
    bill2 = 130 + (50 * 6)  # $130 bill charged a $50 late fee for 6 months
    if overdue_months := 2:
        bill3 = 444 + 40  # $444 bill charged $40 fee for the first late month
    elif overdue_months := 3:
        bill3 = 444 + (40 * 3)  # $444 bill charged twice the $40 fee for the second late month
    else:
        bill3 = 444  # $444 bill not yet past due

    # Calculate the total amount owed on all three bills
    total_bills = bill1 + bill2 + bill3
    result = total_bills
    return result

print(solution())