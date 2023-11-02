def solution():
    
    starting_pay = 10
    first_year_raise = 0.2
    second_year_cut = 0.25
    first_year_pay = starting_pay * (1 + first_year_raise)
    second_year_pay = first_year_pay * (1 - second_year_cut)
    result = second_year_pay
    return result

print(solution())