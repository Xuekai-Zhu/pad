def solution():
    """Sam invested $10,000 and earned 20% interest compounded for 3 years. He then invested more until he had three times as much invested. The next year, he got a 15% return on his investment. How much money does he have now?"""
    # Calculate the amount of money Sam has after 3 years (using compound interest formula)
    initial_investment = 10000
    years = 3
    interest_rate = 0.2
    compounded_interest = initial_investment * (1 + interest_rate)**years

    # Calculate the amount of additional investment needed to have three times the initial investment
    target_investment = initial_investment * 3
    additional_investment = target_investment - compounded_interest

    # Calculate the amount of money Sam has after the additional investment and one year of a 15% return
    total_investment = compounded_interest + additional_investment
    total_investment *= 1.15

    # Return the result
    result = total_investment
    return result

print(solution())