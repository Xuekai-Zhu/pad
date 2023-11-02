def solution():
    # Calculate the amount raised by Miss Rollin's class
    rollin_amount = 3 * 2300

    # Calculate the amount raised by Mrs. Sutton's class
    sutton_amount = rollin_amount / 8

    # Calculate the total amount raised by the school
    total_amount = rollin_amount + sutton_amount + 2300

    # Calculate the administration fees
    admin_fees = total_amount * 0.02

    # Calculate the final amount for the playground
    playground_amount = total_amount - admin_fees
    result = playground_amount
    return result

print(solution())