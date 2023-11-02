def solution():
    """Ian spent half the money he made on doing online surveys. If he worked 8 hours doing surveys and on average he's able to earn $18 per hour doing surveys, how much money does he have left?"""
    # Calculate the total money earned from doing surveys
    total_earned = 18 * 8

    # Calculate the amount spent on surveys
    amount_spent = total_earned / 2

    # Calculate the amount of money remaining
    money_left = total_earned - amount_spent

    # Display the amount of money left
    result = money_left
    return result

print(solution())