def solution():
    """An internet provider gives a 5% discount if the customer pays before the 25th day of the month. If the monthly internet rate is $50, how much did the customer pay in all for 4 months if he paid every 25th of the month?"""
    # Define the monthly internet rate and the discount percentage
    MONTHLY_RATE = 50
    DISCOUNT_PERCENTAGE = 0.05

    # Calculate the discounted rate if paid before the 25th
    discounted_rate = MONTHLY_RATE - (MONTHLY_RATE * DISCOUNT_PERCENTAGE)

    # Calculate the total cost for 4 months
    total_cost = (MONTHLY_RATE * 4) + (discounted_rate * 4)

    # Display the total cost
    result = total_cost
    return result

print(solution())