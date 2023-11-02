def solution():
    """Tony puts $1,000 in a savings account for 1 year. It earns 20% interest. He then takes out half the money to buy a new TV. The next year, the remaining money earns 15% interest. How much is now in the account?"""
    initial_amount = 1000
    first_year_interest = 0.2
    half_amount = initial_amount / 2
    remaining_amount = initial_amount - half_amount
    after_first_year = remaining_amount + (remaining_amount * first_year_interest)
    second_year_interest = 0.15
    final_amount = after_first_year + (after_first_year * second_year_interest)
    result = final_amount
    return result

print(solution())