def solution():
    
    initial_amount = 1000
    first_year_interest = 0.2
    half_amount = initial_amount / 2
    amount_left = initial_amount - half_amount
    first_year_earnings = amount_left * first_year_interest
    amount_after_first_year = amount_left + first_year_earnings
    second_year_interest = 0.15
    second_year_earnings = amount_after_first_year * second_year_interest
    total_amount = amount_after_first_year + second_year_earnings
    result = total_amount
    return result

print(solution())