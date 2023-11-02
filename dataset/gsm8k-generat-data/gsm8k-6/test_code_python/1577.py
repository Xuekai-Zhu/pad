def solution():
    # Calculate the total amount of money in Steve's account after two years
    initial_amount = 100
    yearly_deposit = 10
    interest_rate = 0.1
    amount_after_first_year = initial_amount + yearly_deposit + (initial_amount + yearly_deposit) * interest_rate
    amount_after_two_years = amount_after_first_year + yearly_deposit + (amount_after_first_year + yearly_deposit) * interest_rate
    result = amount_after_two_years
    return result

print(solution())