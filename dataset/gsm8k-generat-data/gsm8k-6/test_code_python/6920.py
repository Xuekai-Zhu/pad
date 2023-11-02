def solution():
    # Calculate the total amount in the bank after two years with interest
    interest_rate = 0.07  # 7% interest rate
    amount_after_one_year = 5600 + (5600 * interest_rate)  # amount after one year with interest
    amount_after_two_years = amount_after_one_year + (amount_after_one_year * interest_rate)  # amount after two years with interest
    result = amount_after_two_years
    return result

print(solution())