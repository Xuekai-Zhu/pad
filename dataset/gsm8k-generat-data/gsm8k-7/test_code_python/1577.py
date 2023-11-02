def solution():
    amount_in_bank = 100
    annual_increase = 10 # amount added each year
    interest_rate = 0.1 # 10% interest rate
    num_years = 2

    # Calculate the total amount added to the account
    total_increase = annual_increase * num_years

    # Calculate the interest earned after 2 years
    interest_earned = (amount_in_bank + total_increase) * interest_rate * num_years

    # Calculate the total amount in the account after 2 years
    total_amount = amount_in_bank + total_increase + interest_earned
    result = total_amount
    return result

print(solution())