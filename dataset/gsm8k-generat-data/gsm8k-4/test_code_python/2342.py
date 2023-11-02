def solution():
    """An internet provider gives a 5% discount if the customer pays before the 25th day of the month. If the monthly internet rate is $50, how much did the customer pay in all for 4 months if he paid every 25th of the month?"""
    # Define the monthly internet rate and the discount percentage
    monthly_rate = 50
    discount_percentage = 0.05

    # Calculate the discounted rate if the customer pays before the 25th
    discounted_rate = monthly_rate - (monthly_rate * discount_percentage)

    # Calculate the total cost for 4 months, assuming the customer pays on the 25th of each month
    total_cost = (monthly_rate * 4) + (discounted_rate * 4)

    result = total_cost
    return result

print(solution())