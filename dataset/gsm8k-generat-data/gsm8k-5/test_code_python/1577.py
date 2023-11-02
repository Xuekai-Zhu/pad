def solution():
    starting_amount = 100  # Steve starts with $100 in his bank account
    yearly_contribution = 10  # Steve puts $10 in his bank account every year
    interest_rate = 0.1  # Steve's bank account earns 10% interest every year
    time_periods = 2  # Steve wants to know how much money is in his account after 2 years

    # Calculate the total amount in Steve's bank account after 2 years
    amount_after_year_1 = starting_amount + yearly_contribution
    amount_after_year_2 = amount_after_year_1 + (amount_after_year_1 * interest_rate) + yearly_contribution
    total_amount = amount_after_year_2

    result = total_amount
    return result

print(solution())