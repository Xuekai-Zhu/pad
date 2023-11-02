def solution():
    # Calculate the amount raised by Miss Rollin's class
    total_amount = (2300 * 2) / (1/8) / (1/3 + 1/8 + 1)
    # Mrs. Johnson's class raised $2300, which is twice the amount that Mrs. Sutton’s class raised
    # Mrs. Sutton’s class raised 8 times less than Miss Rollin’s class
    # Miss Rollin’s class raised a third of the total amount raised by the school

    # Calculate the amount raised by the school (before administration fees deduction)
    total_amount_before_fees = total_amount + 2300 + (total_amount / 8)

    # Calculate the amount of administration fees
    fees = 0.02 * total_amount_before_fees

    # Calculate the total amount raised by the school (after administration fees deduction)
    total_amount_after_fees = total_amount_before_fees - fees

    result = total_amount_after_fees
    return result

print(solution())