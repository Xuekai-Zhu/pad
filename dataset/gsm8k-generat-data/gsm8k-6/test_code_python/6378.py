def solution():
    # Calculate the total amount of money Grant received for his teeth
    total_money = 54 - 20  # the $20 he received for his first tooth is already accounted for
    # Calculate the number of teeth he lost and didn't receive money for
    lost_teeth = 2
    # Calculate the amount of money he received for each tooth
    money_per_tooth = total_money / (20-lost_teeth)
    result = money_per_tooth
    return result

print(solution())