def solution():
    # Calculate the total amount paid by Yoque in 11 months
    total_paid = 15 * 11

    # Calculate the amount borrowed by Yoque
    # We know that the total amount paid is 110% of the amount borrowed
    # So, amount borrowed = total amount paid / 110 * 100
    amount_borrowed = total_paid / 1.1
    result = amount_borrowed
    return result

print(solution())