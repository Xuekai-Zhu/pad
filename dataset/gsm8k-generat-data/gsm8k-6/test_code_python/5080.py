def solution():
    # Calculate the amount of money Zahra received
    zahra_money = 450 - (1/3) * 450  # Zahra received 1/3 less money than Kimmie

    # Calculate the total amount of money saved in their joint account
    joint_savings = (0.5 * 450) + (0.5 * zahra_money)  

    result = joint_savings
    return result

print(solution())