def solution():
    """Ariana is past due on three bills. The first bill for $200 charges 10% simple interest for each overdue month and it's 2 months overdue. The second bill for $130 charges a flat $50 late fee per month and is 6 months overdue. The last bill is two months late and charges a $40 fee the first month overdue and twice that fee the second month overdue and is for $444. How much does Ariana owe in total?"""
    # Calculate the total amount due for the first bill
    bill1_amount = 200 * 1.1 * 2

    # Calculate the total amount due for the second bill
    bill2_amount = 130 + 50 * 6

    # Calculate the total amount due for the third bill
    bill3_amount = 444 + 40 + 2 * 40

    # Calculate the total amount due for all three bills
    total_amount = bill1_amount + bill2_amount + bill3_amount

    # Display the total amount due
    result = total_amount
    return result

print(solution())