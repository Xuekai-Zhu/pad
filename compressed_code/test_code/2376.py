def solution():
    
    starting_amount = 100
    evaporated_amount = starting_amount * 0.2
    remaining_after_one_year = starting_amount - evaporated_amount
    remaining_after_two_years = remaining_after_one_year - (evaporated_amount * remaining_after_one_year / starting_amount)
    percent_remaining = remaining_after_two_years / starting_amount * 100
    result = percent_remaining
    return result

print(solution())