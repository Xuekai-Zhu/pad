def solution():
    """Susie babysits every day for 3 hours a day at the rate of $10 per hour. She spent 3/10 of the money she earned from last week to buy a make-up set. She then spent 2/5 of her money on her skincare products. How much is left from her earnings last week, in dollars?"""
    # Define the variables
    hours_per_day = 3
    rate_per_hour = 10
    money_earned = hours_per_day * rate_per_hour * 7
    make_up_cost = money_earned * 3/10
    skincare_cost = money_earned * 2/5

    # Calculate the remaining amount
    remaining_amount = money_earned - make_up_cost - skincare_cost

    # Display the remaining amount
    result = remaining_amount
    return result

print(solution())