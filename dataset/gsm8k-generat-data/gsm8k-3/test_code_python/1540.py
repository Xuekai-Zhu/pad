def solution():
    """Sam invested $10,000 and earned 20% interest compounded for 3 years. He then invested more until he had three times as much invested. The next year, he got a 15% return on his investment. How much money does he have now?"""
    # Calculate the total amount of money Sam had after 3 years with the initial investment of $10,000 and 20% interest compounded annually
    current_amount = 10000 * (1 + 0.2)**3

    # Calculate how much more Sam needs to invest to have three times as much money as he initially had
    additional_investment = current_amount * 2 / 3

    # Calculate the total amount of money Sam has after making the additional investment
    current_amount += additional_investment

    # Calculate the return Sam gets after one year with a 15% interest rate
    current_amount *= 1 + 0.15

    # Display the current amount of money Sam has
    result = current_amount
    return result

print(solution())