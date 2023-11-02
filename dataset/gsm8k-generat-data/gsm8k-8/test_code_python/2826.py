def solution():
    # Calculate the total number of monthly payments over 5 years
    total_payments = 5 * 12

    # Calculate the total amount paid in monthly payments
    total_payments_amount = total_payments * 600

    # Calculate the total amount borrowed, including the down payment
    total_borrowed = total_payments_amount + 10000

    result = total_borrowed
    return result

print(solution())