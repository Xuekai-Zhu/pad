def solution():
    
    starting_portfolio = 80
    first_year_growth = 0.15
    first_year_ending_portfolio = starting_portfolio * (1 + first_year_growth)
    second_year_contribution = 28
    second_year_growth = 0.1
    final_portfolio = (first_year_ending_portfolio + second_year_contribution) * (1 + second_year_growth)
    result = final_portfolio
    return result

print(solution())