def solution():
    # Calculate Zahra's earnings
    zahra_earnings = 450 - (1/3 * 450)

    # Calculate the total earnings and the amount saved
    total_earnings = kimmie_earnings + zahra_earnings
    amount_saved = 0.5 * total_earnings

    # Calculate the total amount in the joint savings account
    joint_savings = amount_saved * 2
    result = joint_savings
    return result

print(solution())