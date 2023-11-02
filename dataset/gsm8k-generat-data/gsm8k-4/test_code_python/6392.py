def solution():
    """Ariana is past due on three bills. The first bill for $200 charges 10% simple interest for each overdue month and it's 2 months overdue. The second bill for $130 charges a flat $50 late fee per month and is 6 months overdue. The last bill is two months late and charges a $40 fee the first month overdue and twice that fee the second month overdue and is for $444. How much does Ariana owe in total?"""
    
    # Calculate the interest charges for the first bill
    first_bill = 200 * (1 + (0.1 * 2))

    # Calculate the late fees for the second bill
    second_bill = 130 + (50 * 6)

    # Calculate the late fees for the third bill
    third_bill = 444 + 40 + (2 * 40)

    # Calculate total amount due
    total_due = first_bill + second_bill + third_bill

    result = total_due
    return result

print(solution())