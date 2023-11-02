def solution():
    total_borrowed = 0
    total_paid = 0
    payment_per_month = 10
    num_months_passed = 6
    num_months_left = 4

    # Calculate the total amount borrowed
    total_borrowed = payment_per_month * num_months_passed

    # Calculate the total amount paid
    total_paid = payment_per_month * (num_months_passed / 2)

    # Calculate the amount still owed
    amount_owed = total_borrowed - total_paid

    # Calculate the amount that will still be owed after 4 more months
    amount_still_owed = amount_owed - (payment_per_month * num_months_left)
    result = amount_still_owed
    return result

print(solution())