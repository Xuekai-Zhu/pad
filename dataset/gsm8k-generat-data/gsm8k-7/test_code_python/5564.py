def solution():
    # Let x be the total amount raised by the school before administration fees
    # Mrs. Sutton's class raised 8 times less than Miss Rollin's class, so let y be the amount raised by Miss Rollin's class
    # Mrs. Sutton's class raised half of what Mrs. Johnson's class raised, so let z be the amount raised by Mrs. Sutton's class
    # Then we have:

    y = x / 3
    z = (1/2) * (2300)
    total_raised = x + y + z

    admin_fees = 0.02 * total_raised
    total_raised_after_fees = total_raised - admin_fees
    result = total_raised_after_fees

    return result

print(solution())