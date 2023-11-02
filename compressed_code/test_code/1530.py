def solution():
    
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