def solution():
    initial_investment = 1000
    monthly_deposit = 100
    yearly_interest_rate = 0.1
    time_in_years = 2

    # Calculate the total number of deposits made
    total_deposits = 12 * time_in_years

    # Calculate the final amount in the fund
    final_amount = initial_investment * ((1 + yearly_interest_rate / 12) ** total_deposits) +\
                   (monthly_deposit * (((1 + yearly_interest_rate / 12) ** total_deposits) - 1) / (yearly_interest_rate / 12))

    result = final_amount
    return result

print(solution())