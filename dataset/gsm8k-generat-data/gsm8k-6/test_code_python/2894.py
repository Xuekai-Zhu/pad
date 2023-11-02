def solution():
    # Calculate the total amount of money Ian earned
    total_money_earned = 8 * 18  # Ian earns $18 per hour doing surveys and worked for 8 hours

    # Calculate the amount of money Ian spent on doing online surveys
    money_spent = total_money_earned / 2  # Ian spent half the money he made on doing online surveys

    # Calculate the amount of money Ian has left
    money_left = total_money_earned - money_spent

    result = money_left
    return result

print(solution())