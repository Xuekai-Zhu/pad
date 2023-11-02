def solution():
    """Sam invested $10,000 and earned 20% interest compounded for 3 years. He then invested more until he had three times as much invested. 
    The next year, he got a 15% return on his investment. How much money does he have now?"""
    initial_investment = 10000
    interest_rate = 0.2
    years = 3
    final_value = initial_investment * (1 + interest_rate)**years
    additional_investment = final_value * 2 / 3
    total_investment = initial_investment + additional_investment
    new_interest_rate = 0.15
    final_value_after_year = total_investment * (1 + new_interest_rate)
    result = final_value_after_year
    return result

print(solution())