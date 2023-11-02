def solution():
    """The school band is having a car wash to raise money. Their goal is to collect $150. So far they have earned $10 each from three families and $5 each from 15 families. How much more money do they have to earn to reach their goal?"""
    # Calculate the amount of money earned from three families
    family_earnings1 = 10 * 3

    # Calculate the amount of money earned from 15 families
    family_earnings2 = 5 * 15

    # Calculate the total amount of money earned
    total_earnings = family_earnings1 + family_earnings2

    # Calculate the amount of money left to reach the goal
    remaining_amount = 150 - total_earnings

    # Display the remaining amount
    result = remaining_amount
    return result

print(solution())